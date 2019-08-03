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
	globalMinFreq = 432.9
	globalMaxFreq = 433.9
	fontName = '/home/paulo/25to1760MHzSA/fontComputer/cmunsx.ttf'
	imageSource = '/home/paulo/25to1760MHzSA/images/graph.png'
	relGraph = True

	def build(self):

		Clock.schedule_interval(self.update, 2)
		mpl.use("TKAgg")

		return SA251760Gui()

	def update(self, dt):

		sdr = RtlSdr()
		
		# configure device
		sdr.center_freq = ((self.globalMinFreq + self.globalMaxFreq)/2)*1e6
		sdr.gain = 2

		samples = sdr.read_samples(512*1024)
	
		fig = plt.figure()
		fig.patch.set_alpha(0)
	
		prop = fm.FontProperties(fname = self.fontName, size = 14)

		#Axis inputs
		ax = plt.psd(samples, NFFT = 1024, Fc=sdr.center_freq/1e6, color='k')
		ax = plt.xlim(self.globalMinFreq, self.globalMaxFreq)

		#Axis layout
		ax = plt.xlabel('Frequency [MHz]', fontproperties=prop, color='w')
		ax = plt.ylabel('Relative power [dB]', fontproperties=prop, color='w')
		ax = fig.add_subplot(111)
		ax.grid(True, linestyle='-.',color='w')
		ax.tick_params(labelcolor='w', labelsize='medium', width=3)
		ax.patch.set_alpha(0)

		if(self.relGraph == True):
			self.root.ids.graph_kivy.reload()

		plt.plot(433.4, -20, 'v', color='red', ms=10)
		plt.savefig(self.imageSource)

if __name__ == '__main__':
	SA251760App().run()