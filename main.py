from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import ActionGroup
import matplotlib.pyplot as plt
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.garden.graph import Graph, MeshLinePlot
from math import sin

Config.set('kivy','window_icon','path/to/icon.ico')

class SA251760Gui(FloatLayout):
	pass

class RoundedButton(Button):
    pass

class ButtonActBar(ActionButton):
	pass

class ActionGroupCust(ActionGroup):
	pass

class LineRectangle(Widget):
    pass

class SA251760App(App):
	globalMinFreq = 25
	globalMaxFreq = 1760
	plot = plt
	plot.plot([1, 23, 2, 4])
	plot.ylabel('some numbers')
	plt.gcf()
	plt.savefig('/home/paulo/25to1760MHzSA/images/graph.png')
	def build(self):
		return SA251760Gui()

if __name__ == '__main__':
	SA251760App().run()