from abc import ABC, abstractmethod
import threading
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
        self.temperature = Temperature()
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

class Temperature():
    def __init__(self):
        self.value = 100.0
        self.inc = 1
    def get_temperature(self):
        #num = 0
        #while num <= 10:#1000000:
        #    num += 1
        self.value = self.value + self.inc
        if self.value > 103 or self.value < 89:
            self.inc = self.inc * -1
        return self.value
    
# class PressureSensor(Sensor):
#     def __init__(self):
#         super().__init__(update_callback)
#         self.value = 0.0
#         self.temperature = Temperature()
#         self.update_thread = threading.Thread(target=self.update_value, daemon=True)
#         self.update_thread.start() # Запуск потока


#     def get_value(self):
#         return str(int(self.value))
#     def update_value(self):
#         while True:
#             self.value = self.temperature.get_temperature()
#             time.sleep(0.5)
