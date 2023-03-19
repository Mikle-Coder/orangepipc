from enum import Enum

class BUTTON_STATE(Enum):
    ACTIVE = u"QPushButton {background-color:rgb(62, 93, 143);border: none;border-radius: 10px;color: white}"
    INACTIVE =  u"QPushButton {background-color:rgb(46, 69, 107);border: none;border-radius: 10px;color: white}"

class SIZE_CHANGE(Enum):
    UP = BUTTON_STATE.ACTIVE
    DOWN = BUTTON_STATE.INACTIVE

class SignalForm(Enum):
    TRIANGLE = "Треугольный"
    RECTANGULAR = "Прямоугольный"
    SINE = "Синусоидальный"
    SAWTOOTH = "Пилообразный"

class LaunchState(Enum):
    ON = u"QPushButton { background-color: rgb(90, 234, 47); color: rgb(42, 225, 0); border: none; border-radius: 10px; color: white}"
    OFF = u"QPushButton { background-color: rgb(234, 47, 47); color: rgb(42, 225, 0); border: none; border-radius: 10px; color: white}"
    PAUSE = u"QPushButton { background-color: rgb(236, 220, 0); color: rgb(42, 225, 0); border: none; border-radius: 10px; color: white}"

class HeaterState(Enum):
    ON = 1
    OFF = -1