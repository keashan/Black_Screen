# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import kivy
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.lang import Builder

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import notification


Window.clearcolor = (146/255, 233/255, 253/255, 1)

class FirstPage(Screen):
    slider = Slider(value_track=True, value_track_color=[1, 0, 0, 1])
    #slider=ObjectProperty(None)
    #qc=ObjectProperty(None) 
    #sw=ObjectProperty(None)
    
    def quickchange(self):
        #notification.notify(title='Button Clicked',message='Slider Value:' + str(self.slider.value/255),app_icon=None,timeout=100)
        #print('Slider Value:',str(self.slider.value))
        #=self.slider.value
        #blackscreen_app.screen_manager.ids.BackPage.ids.cl.text=slider_value
        
        blackscreen_app.screen_manager.current='BackPage'
        blackscreen_app.screen_manager.transition.direction="right"
        


class BackPage(Screen):
    def on_enter(self,*args):
        slider_value=self.manager.ids.FirstPage.slider.value
        print(slider_value)
        self.cl.text= slider_value

class WindowManager(ScreenManager):
    pass

kv=Builder.load_file("BlackScreen.kv")

class BlackScreenApp(App):
    def build(self):
        self.screen_manager=ScreenManager()

        self.first_page=FirstPage()
        screen=Screen(name="FirstPage")
        screen.add_widget(self.first_page)
        self.screen_manager.add_widget(screen)

        self.back_page=BackPage()
        screen=Screen(name="BackPage")
        screen.add_widget(self.back_page)
        self.screen_manager.add_widget(screen)

        #.screen_manager.current='BackPage'
        return self.screen_manager

    
if __name__=='__main__':
    blackscreen_app=BlackScreenApp()
    blackscreen_app.run()