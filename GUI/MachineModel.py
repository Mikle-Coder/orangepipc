
import sys
from abc import ABC, abstractmethod
from PySide2.QtCore import QTimer, QTime, QObject
from PySide2.QtWidgets import *
import numpy as np
from datetime import *
from SignalGenerator import *
from Parameter import *
from Enums import LaunchState, ControllerState, SignalForm
from MyButton import MyButton
from Mode import *

if sys.platform == 'win32':
    from MixerTest import Mixer
    from SensorTest import TemperatureSensor, PressureSensor
    from PinControlTest import Heater, UltrasonicEmitter
else:
    from Mixer import Mixer
    from Sensor import TemperatureSensor, PressureSensor
    from PinControl import Heater, UltrasonicEmitter

class Model():
    def __init__(self):
        self.modes = None
        self.current_mode_index = 0
        self.modeManager = ModeManager()
        mode = self.modeManager.load_config()

        self.temperature = ParameterWithUnit(current_value = mode.temperature, pitch = 1, unit="\u00b0C",min_value=1, max_value=125)
        self.power = ParameterWithUnit(current_value = mode.power, unit="%", pitch = 1,min_value=1, max_value=100)
        self.frequyncy = ParameterWithUnit(current_value = mode.frequyncy,pitch = 5, unit="kHz",min_value=5, max_value=100)
        self.timer_param = TimerParameter(current_value = mode.timer_param, pitch = 1, min_value = 1, max_value = 60*24)
        self.signal_form = SignalParameter(current_value = mode.signal_form)

        self.timer_duration = 0
        self.current_nav_button = MyButton(loop=False)
        self.current_page = QObject()
        self.current_signal_button = MyButton(loop=False)

        self.signal_generator = SignalGenerator()
        self.mixer = Mixer()
        self.launch_state = LaunchState.OFF
        self.temperature_sensor = TemperatureSensor()
        self.pressure_sensor = PressureSensor()
        self.heater = Heater()
        self.ultrasonicEmitter = UltrasonicEmitter()
        self.temperature_sensor.set_callback(self.check_temperature_threshold)

    def __frequyncy_is_40__(self):
        return self.frequyncy.current_value == 40

    def start(self):
        if self.timer_duration == 0:
            self.timer_duration = self.timer_param.current_value * 60
        self.launch_state = LaunchState.ON
        self.signal_generator.start(self.signal_form.current_value, self.frequyncy.current_value)
        if self.__frequyncy_is_40__():
            self.ultrasonicEmitter.ON()
            self.heater.ON()
    
    def pause(self):
        self.launch_state = LaunchState.PAUSE
        self.signal_generator.stop()
        if self.__frequyncy_is_40__():
            self.ultrasonicEmitter.OFF()
            self.heater.OFF()

    def stop(self):
        self.timer_duration = 0
        self.launch_state = LaunchState.OFF
        self.signal_generator.stop()
        if self.__frequyncy_is_40__():
            self.ultrasonicEmitter.OFF()
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

    def set_active_signal_button(self, button):
        self.current_signal_button = button
    
    def check_temperature_threshold(self):
        if self.launch_state == LaunchState.ON:
            if self.temperature_sensor.value >= self.temperature.current_value and self.heater.state == ControllerState.ON and self.__frequyncy_is_40__():
                self.heater.OFF()
            elif self.temperature_sensor.value < self.temperature.current_value and self.heater.state == ControllerState.OFF and self.__frequyncy_is_40__():
                self.heater.ON()

    def update_params(self, mode : Mode):
        self.temperature.set_value(mode.temperature)
        self.power.set_value(mode.power)
        self.frequyncy.set_value(mode.frequyncy)
        self.timer_param.set_value(mode.timer_param)
        self.signal_form.set_value(mode.signal_form)

    def save_mode(self):
        mode = Mode(self.temperature.current_value,
                    self.power.current_value,
                    self.frequyncy.current_value,
                    self.timer_param.current_value,
                    self.signal_form.current_value)
        
        self.modeManager.update_config(mode)
        return f'Режим {self.modeManager.save_mode_to_file(mode)}\nсохранён'
    
    def load_mode_list(self):
        self.modes = self.modeManager.get_mode_list()

    def clear_modes(self):
        self.modes = None
        self.current_mode_index = 0

    def get_current_mode(self):
        if len(self.modes) > 0: return f'Режим {self.modes[self.current_mode_index].name}'
        else: return "Список пуст" 

    def get_next_mode(self):
        if not (self.current_mode_index + 1 > len(self.modes)-1) : self.current_mode_index += 1
        return self.get_current_mode()

    def get_previous_mode(self):
        if not (self.current_mode_index - 1 < 0) : self.current_mode_index -= 1
        return self.get_current_mode()

    def load_mode(self):
        if len(self.modes) > 0:
            mode = self.modeManager.load_mode_from_file(self.modes[self.current_mode_index].full_path)
            self.update_params(mode)
            self.clear_modes()
            self.modeManager.update_config(mode)
        
