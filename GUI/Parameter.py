from enum import Enum
from FakeABC import FakeABC
from PySide2.QtCore import QObject, Signal
import xml.etree.ElementTree as ET
import os
from abc import abstractmethod  # ABCMeta and ABC are useless
from Enums import SignalForm

class Parameter(QObject, FakeABC):

    value_change_event = Signal()

    def __init__(self, current_value):
        QObject.__init__(self)
        FakeABC.__init__(self)
        self.set_value(current_value)
        
    def set_value(self, value):
        self.current_value = value
        self.value_change_event.emit()

    @abstractmethod
    def get_label_value(self):
        pass

class MeasurableParameter(Parameter):
    def __init__(self, current_value, pitch, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.pitch = pitch
        super().__init__(current_value)

    def set_value(self, value):
        #print(self.min_value,value,self.max_value)
        if value > self.max_value or value < self.min_value:
            return
        super().set_value(value)

    def increment(self):
        self.set_value(self.current_value + self.pitch)
    
    def dicrement(self):
        self.set_value(self.current_value - self.pitch)

class ParameterWithUnit(MeasurableParameter):
    def __init__(self, current_value, pitch, unit, min_value, max_value):
        super().__init__(current_value=current_value, pitch = pitch, min_value = min_value, max_value = max_value)
        self.unit = unit

    def get_label_value(self):
        return str(self.current_value) + " " + self.unit

class TimerParameter(MeasurableParameter):
    def __init__(self, current_value, pitch, min_value, max_value):
        super().__init__(current_value = current_value, pitch = pitch, min_value = min_value, max_value = max_value)

    def get_label_value(self):
        hours, minutes = divmod(int(self.current_value), 60)
        return '{:02d}:{:02d}'.format(hours, minutes)

class SignalParameter(Parameter):
    def __init__(self, current_value : SignalForm = None):
        super().__init__(current_value)
    def get_label_value(self):
        return self.current_value.value
