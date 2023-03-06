from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder

colors = {
    "Teal": {
        "200": "#274a21",
        "500": "#275a21",
        "700": "#274a21",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
	"Green": {
        "200": "#274a21",
        "500": "#274a21",
        "700": "#274a21",
	},
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#242c21", #242c21
        "Background": "#1a1c17",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
}

__events__ = (
    "on_tab_touch_down",
    "on_tab_touch_move",
    "on_tab_touch_up",
    "on_tab_press",
    "on_tab_release",
)

Window.size = (360, 640)

global screen

screen = ScreenManager()

class SplashScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

screen.add_widget(SplashScreen(name="splash_screen"))
screen.add_widget(MainScreen(name="main_screen"))
screen.add_widget(RegisterScreen(name="register_screen"))

class Tab(MDFloatLayout, MDTabsBase):
    pass

class AnimalPerformanceTracker(MDApp):
    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.material_style = "M3"
        return Builder.load_file("telas.kv")

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        if tab_text == "Dashboard":
            screen.current = "dashboard_screen"
        elif tab_text == "Register":
            screen.current = "register_screen"

if __name__ == '__main__':
    AnimalPerformanceTracker().run()
