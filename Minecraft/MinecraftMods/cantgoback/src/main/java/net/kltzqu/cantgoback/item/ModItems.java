package net.kltzqu.cantgoback.item;
import net.kltzqu.cantgoback.cantgoback;
import net.minecraft.world.item.Item;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModItems {


    public static final DeferredRegister<Item> ITEMS =
            DeferredRegister.create(ForgeRegistries.ITEMS, cantgoback.MOD_ID);


    public static void register(IEventBus eventBus) {
        ITEMS.register(eventBus);
    }

    public static final RegistryObject<Item> CLOCK = ITEMS.register("clock",
            () -> new Item(new Item.Properties()

                    .tab(ModCreativeTabs.KL_TAB)
                    .stacksTo(1)
            ));

    public static final RegistryObject<Item> KNIFE = ITEMS.register("knife",
            () -> new Item(new Item.Properties()
                    .tab(ModCreativeTabs.KL_TAB)
                    .stacksTo(1)
                    .durability(100)
            ));

    public static final RegistryObject<Item> GRELKA = ITEMS.register("grelka",
            () -> new Item(new Item.Properties()

                    .tab(ModCreativeTabs.KL_TAB)
                    .stacksTo(1)
                    .durability(250)

            ));

    public static final RegistryObject<Item> SUSY = ITEMS.register("susy",
            () -> new Item(new Item.Properties()
                    .tab(ModCreativeTabs.KL_TAB)
                    .stacksTo(1)
                    .durability(100)
            ));





}
