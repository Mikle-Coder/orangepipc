from pyA20.gpio import gpio
from pyA20.gpio import port
import atexit
from Enums import ControllerState

class PinController:
	def __new__(cls):
		gpio.init()
		return super().__new__(cls)
	
	def __init__(self, port : port):
		gpio.setcfg(port, gpio.OUTPUT)
		self.state = ControllerState.OFF
		atexit.register(self.shutdown)
		
	def shutdown(self):
		self.OFF()
	
	def ON(self):
		gpio.output(port.PA6, gpio.HIGH)
		self.state = ControllerState.ON
		#print("ON")
	
	def OFF(self):
		gpio.output(port.PA6, gpio.LOW)
		self.state = ControllerState.OFF
		#print("OFF")#6

class Heater(PinController):
	def __init__(self):
		super.__init__(port.PA10)

class UltrasonicEmitter(PinController):
	def __init__(self):
		super.__init__(port.PA20)
