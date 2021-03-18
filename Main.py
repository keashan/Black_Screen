# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import kivy
from kivy.app import App
from kivy.uix.slider import Slider

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from kivy.core.window import Window
from plyer import notification


Window.clearcolor = (146/255, 233/255, 253/255, 1)

class MyGrid(Widget):
    slider = Slider(value_track=True, value_track_color=[1, 0, 0, 1])
    #slider=ObjectProperty(None)
    #qc=ObjectProperty(None) 
    #sw=ObjectProperty(None)
    
    def quickchange(self):
        notification.notify(title='Button Clicked',message='Slider Value:',app_icon=None,timeout=100)
        print('Slider Value:',str(int(self.slider.value)))

class BlackScreenApp(App):
    def build(self):
        return MyGrid()
    
if __name__=='__main__':
    BlackScreenApp().run()