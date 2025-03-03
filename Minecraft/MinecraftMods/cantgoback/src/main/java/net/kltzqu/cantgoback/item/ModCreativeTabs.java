package net.kltzqu.cantgoback.item;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventBusSubscriber.Bus;

@Mod.EventBusSubscriber(modid = "cantgobackmod", bus = Bus.MOD)
public class ModCreativeTabs {
    public static final CreativeModeTab KL_TAB = new CreativeModeTab("kl_tab") {
        @Override
        public ItemStack makeIcon() {
            return new ItemStack(ModItems.CLOCK.get()); // Можно заменить на предмет из мода
        }

        @Override
        public Component getDisplayName() {
            return Component.translatable("itemGroup.kl_tab"); // Название вкладки
        }
    };
}
