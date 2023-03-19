import atexit
from Enums import HeaterState

class Heater:
	def __init__(self):
		self.state = HeaterState.OFF
		atexit.register(self.shutdown)
		
	def shutdown(self):
		self.OFF()
	
	def ON(self):
		self.state = HeaterState.ON
		print("ON")
	
	def OFF(self):
		self.state = HeaterState.OFF
		print("OFF")

