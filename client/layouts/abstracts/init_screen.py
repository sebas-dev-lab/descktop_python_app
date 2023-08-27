import kivy  
from kivy.app import App
from kivy.core.window import Window
kivy.require('1.9.0') 
Window.clearcolor = (0, 0, 0, 0)

class InitScreenAPP(App):
    __abstract__ = True

    def build(self):
        pass