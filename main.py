import os
# from kivy.core.window import Window
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

class Live(MDApp, App):
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
    }
    
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.login_screen.loginscreen",
    }
    
    AUTORELOADER_PATHS = [(".", {"recursive": True})]
    
    def build_app(self):
        return Factory.MainScreenManager()
    
Live().run()