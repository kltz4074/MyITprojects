package net.kltzqu.cantgoback.block;

import net.kltzqu.cantgoback.cantgoback;
import net.kltzqu.cantgoback.item.ModCreativeTabs;
import net.kltzqu.cantgoback.item.ModItems;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.function.Supplier;

public class ModBlocks {
    public static final DeferredRegister<Block> BLOCKS =
            DeferredRegister.create(ForgeRegistries.BLOCKS, cantgoback.MOD_ID);

    public static final RegistryObject<Block> SUSYBAKABLOCK = registerBlock("susybakablock",
            () -> new Block(BlockBehaviour.Properties.of(Material.STONE)
                    .jumpFactor(1000000000)
                    .strength(6f).requiresCorrectToolForDrops()) , ModCreativeTabs.KL_TAB
            );

    private static <T extends Block>RegistryObject<T> registerBlock(String name, Supplier<T> block, CreativeModeTab tab) {
        RegistryObject<T> toReturn = BLOCKS.register(name, block);
        registerBlockItem(name, toReturn, ModCreativeTabs.KL_TAB);
        return toReturn;
    }



    private static <T extends Block> RegistryObject<Item> registerBlockItem(String name, RegistryObject<T> block,
                                                                            CreativeModeTab tab ) {
        return ModItems.ITEMS.register(name, () -> new BlockItem(block.get(), new Item.Properties().tab(ModCreativeTabs.KL_TAB)));
    }

    public static void register(IEventBus eventBus) {
        BLOCKS.register(eventBus);
    }

}
