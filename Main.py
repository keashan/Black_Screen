from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


Window.clearcolor = (146/255, 233/255, 253/255, 1)

Builder.load_file("BScreen.kv")

class ColorSelectScreen(Screen):
    pass

class ColorScreen(Screen):
    pass

class BlackScreen(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ColorSelectScreen())
        sm.add_widget(ColorScreen())
        return sm 

if __name__ == '__main__':
    BlackScreen().run()