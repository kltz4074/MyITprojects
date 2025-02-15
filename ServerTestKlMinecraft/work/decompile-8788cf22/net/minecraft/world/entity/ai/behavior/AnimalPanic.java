package net.minecraft.world.entity.ai.behavior;

import com.google.common.collect.ImmutableMap;
import java.util.Optional;
import java.util.function.Predicate;
import javax.annotation.Nullable;
import net.minecraft.core.BlockPosition;
import net.minecraft.server.level.WorldServer;
import net.minecraft.tags.TagsFluid;
import net.minecraft.util.MathHelper;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityCreature;
import net.minecraft.world.entity.ai.BehaviorController;
import net.minecraft.world.entity.ai.memory.MemoryModuleType;
import net.minecraft.world.entity.ai.memory.MemoryStatus;
import net.minecraft.world.entity.ai.memory.MemoryTarget;
import net.minecraft.world.entity.ai.util.LandRandomPos;
import net.minecraft.world.level.IBlockAccess;
import net.minecraft.world.phys.Vec3D;

public class AnimalPanic extends Behavior<EntityCreature> {

    private static final int PANIC_MIN_DURATION = 100;
    private static final int PANIC_MAX_DURATION = 120;
    private static final int PANIC_DISTANCE_HORIZONTAL = 5;
    private static final int PANIC_DISTANCE_VERTICAL = 4;
    private static final Predicate<EntityCreature> DEFAULT_SHOULD_PANIC_PREDICATE = (entitycreature) -> {
        return entitycreature.getLastHurtByMob() != null || entitycreature.isFreezing() || entitycreature.isOnFire();
    };
    private final float speedMultiplier;
    private final Predicate<EntityCreature> shouldPanic;

    public AnimalPanic(float f) {
        this(f, AnimalPanic.DEFAULT_SHOULD_PANIC_PREDICATE);
    }

    public AnimalPanic(float f, Predicate<EntityCreature> predicate) {
        super(ImmutableMap.of(MemoryModuleType.IS_PANICKING, MemoryStatus.REGISTERED, MemoryModuleType.HURT_BY, MemoryStatus.VALUE_PRESENT), 100, 120);
        this.speedMultiplier = f;
        this.shouldPanic = predicate;
    }

    protected boolean checkExtraStartConditions(WorldServer worldserver, EntityCreature entitycreature) {
        return this.shouldPanic.test(entitycreature);
    }

    protected boolean canStillUse(WorldServer worldserver, EntityCreature entitycreature, long i) {
        return true;
    }

    protected void start(WorldServer worldserver, EntityCreature entitycreature, long i) {
        entitycreature.getBrain().setMemory(MemoryModuleType.IS_PANICKING, (Object) true);
        entitycreature.getBrain().eraseMemory(MemoryModuleType.WALK_TARGET);
    }

    protected void stop(WorldServer worldserver, EntityCreature entitycreature, long i) {
        BehaviorController<?> behaviorcontroller = entitycreature.getBrain();

        behaviorcontroller.eraseMemory(MemoryModuleType.IS_PANICKING);
    }

    protected void tick(WorldServer worldserver, EntityCreature entitycreature, long i) {
        if (entitycreature.getNavigation().isDone()) {
            Vec3D vec3d = this.getPanicPos(entitycreature, worldserver);

            if (vec3d != null) {
                entitycreature.getBrain().setMemory(MemoryModuleType.WALK_TARGET, (Object) (new MemoryTarget(vec3d, this.speedMultiplier, 0)));
            }
        }

    }

    @Nullable
    private Vec3D getPanicPos(EntityCreature entitycreature, WorldServer worldserver) {
        if (entitycreature.isOnFire()) {
            Optional<Vec3D> optional = this.lookForWater(worldserver, entitycreature).map(Vec3D::atBottomCenterOf);

            if (optional.isPresent()) {
                return (Vec3D) optional.get();
            }
        }

        return LandRandomPos.getPos(entitycreature, 5, 4);
    }

    private Optional<BlockPosition> lookForWater(IBlockAccess iblockaccess, Entity entity) {
        BlockPosition blockposition = entity.blockPosition();

        if (!iblockaccess.getBlockState(blockposition).getCollisionShape(iblockaccess, blockposition).isEmpty()) {
            return Optional.empty();
        } else {
            Predicate predicate;

            if (MathHelper.ceil(entity.getBbWidth()) == 2) {
                predicate = (blockposition1) -> {
                    return BlockPosition.squareOutSouthEast(blockposition1).allMatch((blockposition2) -> {
                        return iblockaccess.getFluidState(blockposition2).is(TagsFluid.WATER);
                    });
                };
            } else {
                predicate = (blockposition1) -> {
                    return iblockaccess.getFluidState(blockposition1).is(TagsFluid.WATER);
                };
            }

            return BlockPosition.findClosestMatch(blockposition, 5, 1, predicate);
        }
    }
}
