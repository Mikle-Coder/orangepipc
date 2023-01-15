from w1thermsensor import W1ThermSensor as Sen

sensor = Sen()
while(True):
	print(sensor.get_temperature())