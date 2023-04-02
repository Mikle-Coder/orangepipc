from pyA20.gpio import gpio
from pyA20.gpio import port
import atexit
from Enums import HeaterState

class Heater:
	def __init__(self):
		gpio.init()
		gpio.setcfg(port.PA6, gpio.OUTPUT)
		self.state = HeaterState.OFF
		atexit.register(self.shutdown)
		
	def shutdown(self):
		self.OFF()
	
	def ON(self):
		gpio.output(port.PA6, gpio.HIGH)
		self.state = HeaterState.ON
		print("ON")
	
	def OFF(self):
		gpio.output(port.PA6, gpio.LOW)
		self.state = HeaterState.OFF
		print("OFF")#6
