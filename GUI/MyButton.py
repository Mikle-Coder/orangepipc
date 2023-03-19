from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Geometry:
    def __init__(self, x, y, width, height):
            self.x : float = x
            self.y : float = y
            self.height : float = height
            self.width : float = width

    def getQrect(self):
        return QRect(int(self.x), int(self.y), int(self.width), int(self.height))
    
    def setQRect(self, rect : QRect):
        self.x = rect.x()
        self.y = rect.y()
        self.height = rect.height()
        self.width = rect.width()

    def __str__(self):
            string = "X = " + str(self.x) + "\n"
            string += "Y = " + str(self.y) + "\n"
            string += "Width = " + str(self.width) + "\n"
            string += "Height = " + str(self.height) + "\n"
            return string

class MyButton(QPushButton):
    holded = Signal()

    def __init__(self, loop = True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._loop = loop
        self.realGeometry = Geometry(0,0,0,0)
        self.holded.connect(lambda : print("HOLD"))
        
        self.__holding_timer = QTimer(self)
        if loop:
            self.__interval = 500
            self.__holding_timer.timeout.connect(self.__press_automatically)
        else:
            self.__interval = 1000
            self.__holding_timer.timeout.connect(self.hold)

        self.__holding_timer.setInterval(self.__interval)
        self.pressed.connect(self.__holding_timer.start)
        self.released.connect(self.__holding_timer.stop)

    def getRealGeometry(self):
        return Geometry(self.realGeometry.x,
                        self.realGeometry.y,
                        self.realGeometry.width,
                        self.realGeometry.height)
    
    def setRealGeometry(self, value : Geometry):
         self.realGeometry = value
         self.setGeometry(self.realGeometry.getQrect())

    def setGeometry(self, rect):
        if self.realGeometry.width == 0:
            self.realGeometry.setQRect(rect)
        super().setGeometry(rect)
    
    def __press_automatically(self):
        #print("automatically")
        self.pressed.emit()
        if self.__holding_timer.interval() != 50: self.__holding_timer.setInterval(50)
    
    def hold(self):
        print("holded")
        self.holded.emit()
        self.__holding_timer.stop()
        self.released.emit()
        
    def mousePressEvent(self, event):
        #print("pressed")
        self.__holding_timer.start()
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event):
        if self.__holding_timer.isActive():
            #print("released")
            if self._loop : self.__holding_timer.setInterval(self.__interval)
            self.__holding_timer.stop()
            super().mouseReleaseEvent(event)

