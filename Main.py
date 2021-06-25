from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import pyautogui
import os
#from jnius import autoclass, cast


#Window.size = (300, 600)
Window.clearcolor = (146/255, 233/255, 253/255, 1)

Builder.load_file("BScreen.kv")
   
class BlackScreenGUI(BoxLayout):
    sm= ObjectProperty()
    def __init__(self, **kwargs):
        super(BlackScreenGUI, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.hook_keyboard)
        Clock.schedule_once(self.first_screen,5)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
        # do what you want, return True for stopping the propagation
            Clock.schedule_once(self.go_back)
            return True 

    def go_back(self,*args):
        if  self.sm.current !='colorselect':
            self.sm.transition.direction = 'left'
            self.sm.current = self.sm.previous()
    
    def btn_quick(self):
        self.sm.transition.direction = 'right'
        self.sm.current = 'black'

    def btn_wallpaper(self):
        self.sm.transition.direction = 'right'
        self.sm.current = 'black'
        Clock.schedule_once(Change_Wallpaper.capture_screen,1)
        Clock.schedule_once(self.go_back,2)

        

    def splash_screen(self):
        Clock.schedule_once(self.first_screen,1)
    
    def first_screen(self,*args):
        self.sm.current='colorselect'

class Change_Wallpaper():

    def capture_screen(self,*args):
        screenshot=pyautogui.screenshot()
        if not os.path.isdir('BlackScreen'):
            os.mkdir('BlackScreen')

        screenshot.save(r'BlackScreen\blackscreen.png')


class BlackScreen(App):
    def build(self):
        return BlackScreenGUI() 

if __name__ == '__main__':
    BlackScreen().run()