
import sys
from abc import ABC, abstractmethod
from PySide2.QtCore import QTimer, QTime, QObject
from PySide2.QtWidgets import *
import numpy as np
from datetime import *
from SignalGenerator import *
from Parameter import *
from Enums import LaunchState, HeaterState
from MyButton import MyButton

if sys.platform == 'win32':
    from MixerTest import Mixer
    from SensorTest import TemperatureSensor#, PressureSensor
    from HeaterTest import Heater
else:
    from Mixer import Mixer
    from Sensor import TemperatureSensor#, PressureSensor
    from Heater import Heater

class Model():
    def __init__(self):
        self.temperature = ParameterWithUnit(current_value=100, pitch = 1, unit="\u00b0C",min_value=1, max_value=125)
        self.power = ParameterWithUnit(current_value=1, unit="%", pitch = 1,min_value=1, max_value=100)
        self.frequyncy = ParameterWithUnit(current_value=5,pitch = 5, unit="kHz",min_value=5, max_value=100)
        self.timer_param = TimerParameter(current_value = 45, pitch = 1, min_value = 1, max_value = 60*24)
        self.signal_form = SignalParameter()

        self.timer_duration = 0
        self.current_nav_button = MyButton(loop=False)
        self.current_page = QObject()
        self.current_signal_button = MyButton(loop=False)

        self.signal_generator = SignalGenerator()
        self.mixer = Mixer()
        self.launch_state = LaunchState.OFF
        #self.pressure_sensor = PressureSensor(print("pressure_sensor"))
        self.temperature_sensor = TemperatureSensor()
        self.heater = Heater()
        self.temperature_sensor.set_callback(self.check_temperature_threshold)
        self.get_config_mode()      

    def start(self):
        if self.timer_duration == 0:
            self.timer_duration = self.timer_param.current_value * 60
        self.launch_state = LaunchState.ON
        #print("start")
        self.signal_generator.start(self.signal_form.current_value, self.frequyncy.current_value)
        self.heater.ON()
    
    def pause(self):
        self.launch_state = LaunchState.PAUSE
        #print("pause")
        self.signal_generator.stop()
        self.heater.OFF()

    def stop(self):
        self.timer_duration = 0
        self.launch_state = LaunchState.OFF
        #print("stop")
        self.signal_generator.stop()
        self.heater.OFF()

    def handle_launch_button(self, hold : bool = False):
        if hold:
            self.stop()
        elif self.current_page.objectName() == "launch_page":
            if self.launch_state != LaunchState.ON:
                self.start()
            else:
                self.pause()
        
        return self.launch_state 
            
    def set_active_page(self, page):
        self.current_page = page

    def set_active_nav_button(self, button):
        self.current_nav_button = button

    def set_active_signal_form(self, button, signal_form):
        self.current_signal_button = button
        self.signal_form.set_value(signal_form)
    
    def check_temperature_threshold(self):
        if self.launch_state == LaunchState.ON:
            if self.temperature_sensor.value >= self.temperature.current_value and self.heater.state == HeaterState.ON:
                self.heater.OFF()
            elif self.temperature_sensor.value < self.temperature.current_value and self.heater.state == HeaterState.OFF:
                self.heater.ON()
    
    def set_config_mode(self):
        print("Config set")

    def get_config_mode(self):
        print("Config get")

    def save_mode(self):
        self.set_config_mode()
        pass

    def load_mode(self):
        pass
        
