import threading
from w1thermsensor import W1ThermSensor as TempSen
from bme280 import getPressure
from abc import ABC, abstractmethod
import time

class Sensor(ABC):
    def __init__(self):
        self._value = 0.0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.callback()

    @abstractmethod
    def get_value(self):
        pass

class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.temperature = TempSen()
        self.update_thread = threading.Thread(target=self.update_value, daemon=True)
        
    def set_callback(self, callback):
        self.callback = callback
        self.update_thread.start()

    def get_value(self):
        return str(int(self.value))
    
    def update_value(self):
        while True:
            new_value = self.temperature.get_temperature()
            if self.value != new_value:
                self.value = new_value
            time.sleep(0.5)

class PressureSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.update_thread = threading.Thread(target=self.update_value, daemon=True)
        self.callback = self.callback_
        self.update_thread.start()

    def get_value(self):
        return '{:.2f}'.format(self.value-1000)
    
    def update_value(self):
        while True:
            new_value = getPressure()
            if self.value != new_value:
                self.value = new_value
            time.sleep(0.5)
            
    def callback_(self):
        pass
