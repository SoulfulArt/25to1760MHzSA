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
from rtlsdr import *
from kivy.clock import Clock
import matplotlib.font_manager as fm
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
import matplotlib as mpl
import numpy as np
from kivy.properties import ListProperty

#Classes definition
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
	globalMinFreq = 900
	globalMaxFreq = 902
	fontName = '/home/paulo/25to1760MHzSA/fontComputer/cmunsx.ttf'
	imageSource = '/home/paulo/25to1760MHzSA/images/graph.png'
	relGraph = True
	markers = []
	bw = 2 #bandwidth of the RTLSDR2832

	def build(self):

		Clock.schedule_interval(self.update, 2)
	
		return SA251760Gui()

	def update(self, dt):

		x = self.globalMinFreq
		sdr = RtlSdr()

		while x<self.globalMaxFreq - self.bw/2:
		# configure device
			sdr.center_freq = (x + self.bw/2)*1e6
			sdr.set_gain(2)
			samples = sdr.read_samples(512*1024)
	
			#Axis inputs
			ax = plt.psd(samples, NFFT = 1024, Fc=sdr.center_freq/1e6, color='k')

			freq = ax[1]
			pw = ax[0]
		
			x = x + self.bw

		fig = plt.gcf()
		
		plot = MeshLinePlot(color=[1, 0, 0, 1])

		list(zip(freq, pw))

		print(plot.points)

		self.root.ids.graphPlot.add_plot(plot)

		if (self.markers): #if markers isn't empty
			for x in self.markers:
				idw = np.where(freq == x)
				print(pw[idw])
				plt.plot(x, 10*np.log10(pw[idw]), 'v', color='red', ms=10)

if __name__ == '__main__':
	SA251760App().run()