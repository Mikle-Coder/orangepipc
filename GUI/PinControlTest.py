import atexit
from Enums import ControllerState

class PinController:
	def __init__(self, name):
		self.name = name
		self.state = ControllerState.OFF
		atexit.register(self.shutdown)
		
	def shutdown(self):
		self.OFF()
	
	def ON(self):
		self.state = ControllerState.ON
		print(str(self.name) + " ON")
	
	def OFF(self):
		self.state = ControllerState.OFF
		print(str(self.name) + " OFF")

class Heater(PinController):
	def __init__(self):
		super().__init__("PA10")

class UltrasonicEmitter(PinController):
	def __init__(self):
		super().__init__("PA20")
