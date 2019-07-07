from kivy.app import App
from kivy.uix.widget import Widget

class SA251760Gui(Widget):
	pass


class SA251760App(App):
	def build(self):
		return SA251760Gui()


if __name__ == '__main__':
	SA251760App().run()