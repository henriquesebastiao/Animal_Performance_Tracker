from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

colors = {
    "Teal": {
        "200": "#274a21",
        "500": "#274a21",
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

Window.size = (360, 640)

global screen

screen = ScreenManager()

class SplashScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

screen.add_widget(SplashScreen(name="splash_screen"))
screen.add_widget(DashboardScreen(name="dashboard_screen"))

class AnimalPerformanceTracker(MDApp):
    
    data = {
		'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
	}
    
    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.material_style = "M3"
        
        return Builder.load_file("telas.kv")

if __name__ == '__main__':
    AnimalPerformanceTracker().run()
