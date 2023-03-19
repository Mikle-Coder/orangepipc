from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from GUI_2_1_1 import *
from MachineControl import Control
from MachineModel import Model
import sys

#print(sys.argv)
app = QApplication(sys.argv)
Form = QWidget()
Form.setWindowFlags(Qt.FramelessWindowHint)
Form.setAttribute(Qt.WA_TranslucentBackground)
view = Ui_MainWindow()
view.setupUi(Form)
model = Model()
control = Control(model = model, view = view)

Form.showFullScreen()
sys.exit(app.exec_())
