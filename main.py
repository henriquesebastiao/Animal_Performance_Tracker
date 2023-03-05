from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder

Window.size = (360, 640)

global screen

screen = ScreenManager()

class SplashScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

screen.add_widget(SplashScreen(name="splash_screen"))
screen.add_widget(LoginScreen(name="login_screen"))

class AnimalPerformanceTracker(MDApp):
    def build(self):
        return Builder.load_file("telas.kv")

if __name__ == '__main__':
    AnimalPerformanceTracker().run()