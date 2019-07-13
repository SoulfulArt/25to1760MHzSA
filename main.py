from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import matplotlib.pyplot as plt
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class SA251760Gui(FloatLayout):
	global globalMinFreq
	global globalMaxFreq 
	
class RoundedButton(Button):
    pass

class LineRectangle(Widget):
    pass

class SA251760App(App):
	globalMinFreq = 25
	globalMaxFreq = 1760
	def build(self):
		return SA251760Gui()

if __name__ == '__main__':
	SA251760App().run()