package net.minecraft.world.level.block.entity;

import javax.annotation.Nullable;
import net.minecraft.advancements.CriterionTriggers;
import net.minecraft.core.BlockPosition;
import net.minecraft.core.NonNullList;
import net.minecraft.nbt.NBTTagCompound;
import net.minecraft.resources.MinecraftKey;
import net.minecraft.server.level.EntityPlayer;
import net.minecraft.server.level.WorldServer;
import net.minecraft.util.RandomSource;
import net.minecraft.world.ContainerUtil;
import net.minecraft.world.IInventory;
import net.minecraft.world.entity.player.EntityHuman;
import net.minecraft.world.entity.player.PlayerInventory;
import net.minecraft.world.inventory.Container;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.IBlockAccess;
import net.minecraft.world.level.block.state.IBlockData;
import net.minecraft.world.level.storage.loot.LootParams;
import net.minecraft.world.level.storage.loot.LootTable;
import net.minecraft.world.level.storage.loot.parameters.LootContextParameterSets;
import net.minecraft.world.level.storage.loot.parameters.LootContextParameters;
import net.minecraft.world.phys.Vec3D;

public abstract class TileEntityLootable extends TileEntityContainer {

    public static final String LOOT_TABLE_TAG = "LootTable";
    public static final String LOOT_TABLE_SEED_TAG = "LootTableSeed";
    @Nullable
    public MinecraftKey lootTable;
    public long lootTableSeed;

    protected TileEntityLootable(TileEntityTypes<?> tileentitytypes, BlockPosition blockposition, IBlockData iblockdata) {
        super(tileentitytypes, blockposition, iblockdata);
    }

    public static void setLootTable(IBlockAccess iblockaccess, RandomSource randomsource, BlockPosition blockposition, MinecraftKey minecraftkey) {
        TileEntity tileentity = iblockaccess.getBlockEntity(blockposition);

        if (tileentity instanceof TileEntityLootable) {
            ((TileEntityLootable) tileentity).setLootTable(minecraftkey, randomsource.nextLong());
        }

    }

    protected boolean tryLoadLootTable(NBTTagCompound nbttagcompound) {
        if (nbttagcompound.contains("LootTable", 8)) {
            this.lootTable = new MinecraftKey(nbttagcompound.getString("LootTable"));
            this.lootTableSeed = nbttagcompound.getLong("LootTableSeed");
            return true;
        } else {
            return false;
        }
    }

    protected boolean trySaveLootTable(NBTTagCompound nbttagcompound) {
        if (this.lootTable == null) {
            return false;
        } else {
            nbttagcompound.putString("LootTable", this.lootTable.toString());
            if (this.lootTableSeed != 0L) {
                nbttagcompound.putLong("LootTableSeed", this.lootTableSeed);
            }

            return true;
        }
    }

    public void unpackLootTable(@Nullable EntityHuman entityhuman) {
        if (this.lootTable != null && this.level.getServer() != null) {
            LootTable loottable = this.level.getServer().getLootData().getLootTable(this.lootTable);

            if (entityhuman instanceof EntityPlayer) {
                CriterionTriggers.GENERATE_LOOT.trigger((EntityPlayer) entityhuman, this.lootTable);
            }

            this.lootTable = null;
            LootParams.a lootparams_a = (new LootParams.a((WorldServer) this.level)).withParameter(LootContextParameters.ORIGIN, Vec3D.atCenterOf(this.worldPosition));

            if (entityhuman != null) {
                lootparams_a.withLuck(entityhuman.getLuck()).withParameter(LootContextParameters.THIS_ENTITY, entityhuman);
            }

            loottable.fill(this, lootparams_a.create(LootContextParameterSets.CHEST), this.lootTableSeed);
        }

    }

    public void setLootTable(MinecraftKey minecraftkey, long i) {
        this.lootTable = minecraftkey;
        this.lootTableSeed = i;
    }

    @Override
    public boolean isEmpty() {
        this.unpackLootTable((EntityHuman) null);
        return this.getItems().stream().allMatch(ItemStack::isEmpty);
    }

    @Override
    public ItemStack getItem(int i) {
        this.unpackLootTable((EntityHuman) null);
        return (ItemStack) this.getItems().get(i);
    }

    @Override
    public ItemStack removeItem(int i, int j) {
        this.unpackLootTable((EntityHuman) null);
        ItemStack itemstack = ContainerUtil.removeItem(this.getItems(), i, j);

        if (!itemstack.isEmpty()) {
            this.setChanged();
        }

        return itemstack;
    }

    @Override
    public ItemStack removeItemNoUpdate(int i) {
        this.unpackLootTable((EntityHuman) null);
        return ContainerUtil.takeItem(this.getItems(), i);
    }

    @Override
    public void setItem(int i, ItemStack itemstack) {
        this.unpackLootTable((EntityHuman) null);
        this.getItems().set(i, itemstack);
        if (itemstack.getCount() > this.getMaxStackSize()) {
            itemstack.setCount(this.getMaxStackSize());
        }

        this.setChanged();
    }

    @Override
    public boolean stillValid(EntityHuman entityhuman) {
        return IInventory.stillValidBlockEntity(this, entityhuman);
    }

    @Override
    public void clearContent() {
        this.getItems().clear();
    }

    protected abstract NonNullList<ItemStack> getItems();

    protected abstract void setItems(NonNullList<ItemStack> nonnulllist);

    @Override
    public boolean canOpen(EntityHuman entityhuman) {
        return super.canOpen(entityhuman) && (this.lootTable == null || !entityhuman.isSpectator());
    }

    @Nullable
    @Override
    public Container createMenu(int i, PlayerInventory playerinventory, EntityHuman entityhuman) {
        if (this.canOpen(entityhuman)) {
            this.unpackLootTable(playerinventory.player);
            return this.createMenu(i, playerinventory);
        } else {
            return null;
        }
    }
}
