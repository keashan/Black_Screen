# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

#from kivy.core.window import Window

#Window.clearcolor = (1, 1, 1, 1)

class MyGrid(Widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__=='__main__':
    MyApp().run()




