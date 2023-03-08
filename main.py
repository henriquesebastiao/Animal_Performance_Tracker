from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder

colors = {
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

Window.size = (360, 640)

global screen
screen = ScreenManager()

class MainScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

# Adicionando as telas ao gerenciador de telas
screen.add_widget(MainScreen(name="main_screen"))
screen.add_widget(RegisterScreen(name="register_screen"))

class Tab(MDFloatLayout, MDTabsBase):
    pass

# Classe principal
class AnimalPerformanceTracker(MDApp):
    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.material_style = "M3"
        return Builder.load_file("telas.kv")

=
# Iniciando o aplicativo
if __name__ == '__main__':
    AnimalPerformanceTracker().run()

print(f"{}")