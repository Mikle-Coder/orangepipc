from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from custom_qstacked_widgets import *
from MyButton import MyButton, Geometry
from Enums import BUTTON_STATE, SIZE_CHANGE, LaunchState


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QSize(320, 240))
        MainWindow.setMaximumSize(QSize(320, 240))
        MainWindow.setBaseSize(QSize(320, 240))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.559, y1:1, x2:0.548, y2:0, stop:0 rgba(39, 58, 89, 255), stop:1 rgba(27, 39, 65, 255));")
        self.pages_widget = QWidget(MainWindow)
        self.pages_widget.setObjectName(u"pages_widget")
        self.pages_widget.setLayoutDirection(Qt.RightToLeft)
        self.pages_widget.setStyleSheet(u"")
        self.menu_frame = QFrame(self.pages_widget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(0, -5, 81, 254))
        self.menu_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.signal_nav_button = MyButton(loop = False, parent = self.menu_frame)
        self.signal_nav_button.setObjectName(u"signal_nav_button")
        self.signal_nav_button.setEnabled(True)
        self.signal_nav_button.setGeometry(QRect(12, 14, 57, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signal_nav_button.sizePolicy().hasHeightForWidth())
        self.signal_nav_button.setSizePolicy(sizePolicy)
        self.signal_nav_button.setMinimumSize(QSize(57, 35))
        self.signal_nav_button.setFocusPolicy(Qt.NoFocus)
        self.signal_nav_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../GUI/Final_Images/signal_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signal_nav_button.setIcon(icon)
        self.signal_nav_button.setIconSize(QSize(35, 35))
        self.frequyncy_and_power_nav_button = MyButton(loop = False, parent = self.menu_frame)
        self.frequyncy_and_power_nav_button.setObjectName(u"frequyncy_and_power_nav_button")
        self.frequyncy_and_power_nav_button.setGeometry(QRect(12, 58, 57, 35))
        sizePolicy.setHeightForWidth(self.frequyncy_and_power_nav_button.sizePolicy().hasHeightForWidth())
        self.frequyncy_and_power_nav_button.setSizePolicy(sizePolicy)
        self.frequyncy_and_power_nav_button.setMinimumSize(QSize(57, 35))
        self.frequyncy_and_power_nav_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../GUI/Final_Images/frequyncy_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frequyncy_and_power_nav_button.setIcon(icon1)
        self.frequyncy_and_power_nav_button.setIconSize(QSize(35, 35))
        self.frequyncy_and_power_nav_button.setFlat(False)
        self.temperature_nav_button = MyButton(loop = False, parent = self.menu_frame)
        self.temperature_nav_button.setObjectName(u"temperature_nav_button")
        self.temperature_nav_button.setGeometry(QRect(12, 102, 57, 35))
        sizePolicy.setHeightForWidth(self.temperature_nav_button.sizePolicy().hasHeightForWidth())
        self.temperature_nav_button.setSizePolicy(sizePolicy)
        self.temperature_nav_button.setMinimumSize(QSize(57, 35))
        self.temperature_nav_button.setLayoutDirection(Qt.LeftToRight)
        self.temperature_nav_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../GUI/Final_Images/temperature_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.temperature_nav_button.setIcon(icon2)
        self.temperature_nav_button.setIconSize(QSize(35, 35))
        self.temperature_nav_button.setChecked(False)
        self.timer_nav_button = MyButton(loop = False, parent = self.menu_frame)
        self.timer_nav_button.setObjectName(u"timer_nav_button")
        self.timer_nav_button.setGeometry(QRect(12, 146, 57, 35))
        sizePolicy.setHeightForWidth(self.timer_nav_button.sizePolicy().hasHeightForWidth())
        self.timer_nav_button.setSizePolicy(sizePolicy)
        self.timer_nav_button.setMinimumSize(QSize(57, 35))
        self.timer_nav_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../../GUI/Final_Images/clock_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.timer_nav_button.setIcon(icon3)
        self.timer_nav_button.setIconSize(QSize(35, 35))
        self.timer_nav_button.setCheckable(False)
        self.launch_button = MyButton(loop = False, parent = self.menu_frame)
        self.launch_button.setObjectName(u"launch_button")
        self.launch_button.setGeometry(QRect(12, 190, 57, 47))
        sizePolicy.setHeightForWidth(self.launch_button.sizePolicy().hasHeightForWidth())
        self.launch_button.setSizePolicy(sizePolicy)
        self.launch_button.setMinimumSize(QSize(57, 45))
        self.launch_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(234, 47, 47);\n"
"	color: rgb(42, 225, 0);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../../GUI/Final_Images/launch_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.launch_button.setIcon(icon4)
        self.launch_button.setIconSize(QSize(40, 40))
        self.pages = QStackedWidget(self.pages_widget)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(79, -1, 241, 243))
        self.pages.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.signal_page = QWidget()
        self.signal_page.setObjectName(u"signal_page")
        self.signal_page.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.signal_frame = QFrame(self.signal_page)
        self.signal_frame.setObjectName(u"signal_frame")
        self.signal_frame.setGeometry(QRect(0, 0, 241, 208))
        self.signal_frame.setMinimumSize(QSize(241, 208))
        self.signal_frame.setMaximumSize(QSize(16777215, 208))
        self.signal_frame.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.signal_frame.setFrameShape(QFrame.StyledPanel)
        self.signal_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.signal_frame)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.signal_frame_label = QLabel(self.signal_frame)
        self.signal_frame_label.setObjectName(u"signal_frame_label")
        self.signal_frame_label.setMaximumSize(QSize(16777215, 23))
        font = QFont()
        font.setFamily(u"Tovari Sans")
        font.setPointSize(19)
        self.signal_frame_label.setFont(font)
        self.signal_frame_label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.signal_frame_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.signal_frame_label)

        self.signal_buttons_frame = QFrame(self.signal_frame)
        self.signal_buttons_frame.setObjectName(u"signal_buttons_frame")
        self.signal_buttons_frame.setEnabled(True)
        self.signal_buttons_frame.setMinimumSize(QSize(0, 170))
        self.signal_buttons_frame.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.signal_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.signal_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.signal_buttons_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.signal_button_0 = MyButton(loop = False, parent = self.signal_buttons_frame)
        self.signal_button_0.setObjectName(u"signal_button_0")
        self.signal_button_0.setEnabled(True)
        sizePolicy.setHeightForWidth(self.signal_button_0.sizePolicy().hasHeightForWidth())
        self.signal_button_0.setSizePolicy(sizePolicy)
        self.signal_button_0.setMinimumSize(QSize(1, 1))
        font1 = QFont()
        font1.setFamily(u"Tovari Sans")
        font1.setPointSize(17)
        self.signal_button_0.setFont(font1)
        self.signal_button_0.setFocusPolicy(Qt.NoFocus)
        self.signal_button_0.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        self.signal_button_0.setIconSize(QSize(0, 45))

        self.verticalLayout_7.addWidget(self.signal_button_0)

        self.signal_button_1 = MyButton(loop = False, parent = self.signal_buttons_frame)
        self.signal_button_1.setObjectName(u"signal_button_1")
        self.signal_button_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.signal_button_1.sizePolicy().hasHeightForWidth())
        self.signal_button_1.setSizePolicy(sizePolicy)
        self.signal_button_1.setMinimumSize(QSize(1, 1))
        self.signal_button_1.setFont(font1)
        self.signal_button_1.setFocusPolicy(Qt.NoFocus)
        self.signal_button_1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        self.signal_button_1.setIconSize(QSize(45, 45))

        self.verticalLayout_7.addWidget(self.signal_button_1)

        self.signal_button_2 = MyButton(loop = False, parent = self.signal_buttons_frame)
        self.signal_button_2.setObjectName(u"signal_button_2")
        self.signal_button_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.signal_button_2.sizePolicy().hasHeightForWidth())
        self.signal_button_2.setSizePolicy(sizePolicy)
        self.signal_button_2.setMinimumSize(QSize(1, 1))
        self.signal_button_2.setFont(font1)
        self.signal_button_2.setFocusPolicy(Qt.NoFocus)
        self.signal_button_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        self.signal_button_2.setIconSize(QSize(45, 45))

        self.verticalLayout_7.addWidget(self.signal_button_2)

        self.signal_button_3 = MyButton(loop = False, parent = self.signal_buttons_frame)
        self.signal_button_3.setObjectName(u"signal_button_3")
        self.signal_button_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.signal_button_3.sizePolicy().hasHeightForWidth())
        self.signal_button_3.setSizePolicy(sizePolicy)
        self.signal_button_3.setMinimumSize(QSize(1, 1))
        self.signal_button_3.setFont(font1)
        self.signal_button_3.setFocusPolicy(Qt.NoFocus)
        self.signal_button_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}")
        self.signal_button_3.setIconSize(QSize(45, 45))

        self.verticalLayout_7.addWidget(self.signal_button_3)


        self.verticalLayout_3.addWidget(self.signal_buttons_frame)

        self.pages.addWidget(self.signal_page)
        self.frequyncy_and_power_page = QWidget()
        self.frequyncy_and_power_page.setObjectName(u"frequyncy_and_power_page")
        self.frequyncy_and_power_page.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.frequyncy_and_power_frame = QFrame(self.frequyncy_and_power_page)
        self.frequyncy_and_power_frame.setObjectName(u"frequyncy_and_power_frame")
        self.frequyncy_and_power_frame.setGeometry(QRect(0, 0, 241, 208))
        self.frequyncy_and_power_frame.setMinimumSize(QSize(241, 208))
        self.frequyncy_and_power_frame.setMaximumSize(QSize(0, 208))
        self.frequyncy_and_power_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.frequyncy_and_power_frame.setFrameShape(QFrame.StyledPanel)
        self.frequyncy_and_power_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frequyncy_and_power_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frequyncy_and_power_label = QLabel(self.frequyncy_and_power_frame)
        self.frequyncy_and_power_label.setObjectName(u"frequyncy_and_power_label")
        self.frequyncy_and_power_label.setMinimumSize(QSize(225, 20))
        self.frequyncy_and_power_label.setMaximumSize(QSize(16777215, 16777215))
        self.frequyncy_and_power_label.setFont(font)
        self.frequyncy_and_power_label.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frequyncy_and_power_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.frequyncy_and_power_label)

        self.empty_frame = QFrame(self.frequyncy_and_power_frame)
        self.empty_frame.setObjectName(u"empty_frame")
        self.empty_frame.setMinimumSize(QSize(0, 15))
        self.empty_frame.setMaximumSize(QSize(10, 16777215))
        self.empty_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.empty_frame.setFrameShape(QFrame.StyledPanel)
        self.empty_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.empty_frame)

        self.frequyncy_and_power_frame_with_buttons_and_info = QFrame(self.frequyncy_and_power_frame)
        self.frequyncy_and_power_frame_with_buttons_and_info.setObjectName(u"frequyncy_and_power_frame_with_buttons_and_info")
        self.frequyncy_and_power_frame_with_buttons_and_info.setMinimumSize(QSize(223, 152))
        self.frequyncy_and_power_frame_with_buttons_and_info.setMaximumSize(QSize(16777215, 160))
        self.frequyncy_and_power_frame_with_buttons_and_info.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.frequyncy_and_power_frame_with_buttons_and_info.setFrameShape(QFrame.StyledPanel)
        self.frequyncy_and_power_frame_with_buttons_and_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frequyncy_and_power_frame_with_buttons_and_info)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frequyncy_and_power_frame_with_buttons = QFrame(self.frequyncy_and_power_frame_with_buttons_and_info)
        self.frequyncy_and_power_frame_with_buttons.setObjectName(u"frequyncy_and_power_frame_with_buttons")
        self.frequyncy_and_power_frame_with_buttons.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.frequyncy_and_power_frame_with_buttons.setFrameShape(QFrame.StyledPanel)
        self.frequyncy_and_power_frame_with_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frequyncy_and_power_frame_with_buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.power_buttons_frame = QFrame(self.frequyncy_and_power_frame_with_buttons)
        self.power_buttons_frame.setObjectName(u"power_buttons_frame")
        self.power_buttons_frame.setMinimumSize(QSize(0, 132))
        self.power_buttons_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.power_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.power_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.power_buttons_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.power_plus_button = MyButton(self.power_buttons_frame)
        self.power_plus_button.setObjectName(u"power_plus_button")
        sizePolicy.setHeightForWidth(self.power_plus_button.sizePolicy().hasHeightForWidth())
        self.power_plus_button.setSizePolicy(sizePolicy)
        self.power_plus_button.setMinimumSize(QSize(50, 50))
        self.power_plus_button.setMaximumSize(QSize(50, 50))
        font2 = QFont()
        font2.setFamily(u"Tovari Sans")
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setWeight(75)
        self.power_plus_button.setFont(font2)
        self.power_plus_button.setLayoutDirection(Qt.LeftToRight)
        self.power_plus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.power_plus_button.setIconSize(QSize(35, 35))
        self.power_plus_button.setChecked(False)

        self.verticalLayout_10.addWidget(self.power_plus_button)

        self.power_minus_button = MyButton(self.power_buttons_frame)
        self.power_minus_button.setObjectName(u"power_minus_button")
        sizePolicy.setHeightForWidth(self.power_minus_button.sizePolicy().hasHeightForWidth())
        self.power_minus_button.setSizePolicy(sizePolicy)
        self.power_minus_button.setMinimumSize(QSize(50, 50))
        self.power_minus_button.setMaximumSize(QSize(50, 50))
        font3 = QFont()
        font3.setFamily(u"Tovari Sans")
        font3.setPointSize(26)
        font3.setBold(True)
        font3.setWeight(75)
        self.power_minus_button.setFont(font3)
        self.power_minus_button.setLayoutDirection(Qt.LeftToRight)
        self.power_minus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.power_minus_button.setIconSize(QSize(35, 35))
        self.power_minus_button.setChecked(False)

        self.verticalLayout_10.addWidget(self.power_minus_button)


        self.horizontalLayout_4.addWidget(self.power_buttons_frame)

        self.empty_frame2 = QFrame(self.frequyncy_and_power_frame_with_buttons)
        self.empty_frame2.setObjectName(u"empty_frame2")
        self.empty_frame2.setMinimumSize(QSize(20, 0))
        self.empty_frame2.setMaximumSize(QSize(0, 16777215))
        self.empty_frame2.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.empty_frame2.setFrameShape(QFrame.StyledPanel)
        self.empty_frame2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.empty_frame2)

        self.frequyncy_buttons_frame = QFrame(self.frequyncy_and_power_frame_with_buttons)
        self.frequyncy_buttons_frame.setObjectName(u"frequyncy_buttons_frame")
        self.frequyncy_buttons_frame.setMinimumSize(QSize(0, 132))
        self.frequyncy_buttons_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.frequyncy_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.frequyncy_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frequyncy_buttons_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frequyncy_plus_button = MyButton(self.frequyncy_buttons_frame)
        self.frequyncy_plus_button.setObjectName(u"frequyncy_plus_button")
        sizePolicy.setHeightForWidth(self.frequyncy_plus_button.sizePolicy().hasHeightForWidth())
        self.frequyncy_plus_button.setSizePolicy(sizePolicy)
        self.frequyncy_plus_button.setMinimumSize(QSize(50, 50))
        self.frequyncy_plus_button.setMaximumSize(QSize(50, 50))
        self.frequyncy_plus_button.setFont(font2)
        self.frequyncy_plus_button.setLayoutDirection(Qt.LeftToRight)
        self.frequyncy_plus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.frequyncy_plus_button.setIconSize(QSize(35, 35))
        self.frequyncy_plus_button.setChecked(False)

        self.verticalLayout_9.addWidget(self.frequyncy_plus_button, 0, Qt.AlignHCenter)

        self.frequyncy_minus_button = MyButton(self.frequyncy_buttons_frame)
        self.frequyncy_minus_button.setObjectName(u"frequyncy_minus_button")
        sizePolicy.setHeightForWidth(self.frequyncy_minus_button.sizePolicy().hasHeightForWidth())
        self.frequyncy_minus_button.setSizePolicy(sizePolicy)
        self.frequyncy_minus_button.setMinimumSize(QSize(50, 50))
        self.frequyncy_minus_button.setMaximumSize(QSize(50, 50))
        self.frequyncy_minus_button.setFont(font3)
        self.frequyncy_minus_button.setLayoutDirection(Qt.LeftToRight)
        self.frequyncy_minus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.frequyncy_minus_button.setIconSize(QSize(35, 35))
        self.frequyncy_minus_button.setChecked(False)

        self.verticalLayout_9.addWidget(self.frequyncy_minus_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frequyncy_buttons_frame)


        self.verticalLayout_6.addWidget(self.frequyncy_and_power_frame_with_buttons)


        self.verticalLayout_4.addWidget(self.frequyncy_and_power_frame_with_buttons_and_info)

        self.frequyncy_value = QLabel(self.frequyncy_and_power_page)
        self.frequyncy_value.setObjectName(u"frequyncy_value")
        self.frequyncy_value.setGeometry(QRect(11, 45, 111, 31))
        self.frequyncy_value.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setFamily(u"Tovari Sans")
        font4.setPointSize(24)
        self.frequyncy_value.setFont(font4)
        self.frequyncy_value.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(102, 239, 254);\n"
"}")
        self.frequyncy_value.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.power_value = QLabel(self.frequyncy_and_power_page)
        self.power_value.setObjectName(u"power_value")
        self.power_value.setGeometry(QRect(132, 45, 91, 31))
        self.power_value.setMinimumSize(QSize(0, 20))
        self.power_value.setFont(font4)
        self.power_value.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(254, 87, 246)\n"
"}")
        self.power_value.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.pages.addWidget(self.frequyncy_and_power_page)
        self.temperature_page = QWidget()
        self.temperature_page.setObjectName(u"temperature_page")
        self.temperature_page.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.temperature_frame = QFrame(self.temperature_page)
        self.temperature_frame.setObjectName(u"temperature_frame")
        self.temperature_frame.setGeometry(QRect(0, 0, 241, 208))
        self.temperature_frame.setMinimumSize(QSize(241, 208))
        self.temperature_frame.setMaximumSize(QSize(16777215, 208))
        self.temperature_frame.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.temperature_frame.setFrameShape(QFrame.StyledPanel)
        self.temperature_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.temperature_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.temperature_frame_label = QLabel(self.temperature_frame)
        self.temperature_frame_label.setObjectName(u"temperature_frame_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.temperature_frame_label.sizePolicy().hasHeightForWidth())
        self.temperature_frame_label.setSizePolicy(sizePolicy1)
        self.temperature_frame_label.setMinimumSize(QSize(0, 33))
        self.temperature_frame_label.setFont(font)
        self.temperature_frame_label.setLayoutDirection(Qt.RightToLeft)
        self.temperature_frame_label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.temperature_frame_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.temperature_frame_label)

        self.temperature_frame_with_buttons_and_info = QFrame(self.temperature_frame)
        self.temperature_frame_with_buttons_and_info.setObjectName(u"temperature_frame_with_buttons_and_info")
        self.temperature_frame_with_buttons_and_info.setMinimumSize(QSize(223, 159))
        self.temperature_frame_with_buttons_and_info.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.temperature_frame_with_buttons_and_info.setFrameShape(QFrame.StyledPanel)
        self.temperature_frame_with_buttons_and_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.temperature_frame_with_buttons_and_info)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.temperature_buttons_frame = QFrame(self.temperature_frame_with_buttons_and_info)
        self.temperature_buttons_frame.setObjectName(u"temperature_buttons_frame")
        self.temperature_buttons_frame.setStyleSheet(u"background-color: rgba(0,0,0,0);")
        self.temperature_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.temperature_buttons_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.temperature_buttons_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.temperature_plus_button = MyButton(self.temperature_buttons_frame)
        self.temperature_plus_button.setObjectName(u"temperature_plus_button")
        sizePolicy.setHeightForWidth(self.temperature_plus_button.sizePolicy().hasHeightForWidth())
        self.temperature_plus_button.setSizePolicy(sizePolicy)
        self.temperature_plus_button.setMinimumSize(QSize(50, 50))
        self.temperature_plus_button.setMaximumSize(QSize(50, 50))
        self.temperature_plus_button.setFont(font2)
        self.temperature_plus_button.setLayoutDirection(Qt.LeftToRight)
        self.temperature_plus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.temperature_plus_button.setIconSize(QSize(35, 35))
        self.temperature_plus_button.setChecked(False)

        self.gridLayout_4.addWidget(self.temperature_plus_button, 0, 0, 1, 1)

        self.temperature_minus_button = MyButton(self.temperature_buttons_frame)
        self.temperature_minus_button.setObjectName(u"temperature_minus_button")
        sizePolicy.setHeightForWidth(self.temperature_minus_button.sizePolicy().hasHeightForWidth())
        self.temperature_minus_button.setSizePolicy(sizePolicy)
        self.temperature_minus_button.setMinimumSize(QSize(50, 50))
        self.temperature_minus_button.setMaximumSize(QSize(50, 50))
        self.temperature_minus_button.setFont(font3)
        self.temperature_minus_button.setLayoutDirection(Qt.LeftToRight)
        self.temperature_minus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.temperature_minus_button.setIconSize(QSize(35, 35))
        self.temperature_minus_button.setChecked(False)

        self.gridLayout_4.addWidget(self.temperature_minus_button, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.temperature_buttons_frame)

        self.temperature_info_frame = QFrame(self.temperature_frame_with_buttons_and_info)
        self.temperature_info_frame.setObjectName(u"temperature_info_frame")
        self.temperature_info_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.temperature_info_frame.setFrameShape(QFrame.StyledPanel)
        self.temperature_info_frame.setFrameShadow(QFrame.Raised)
        self.temperature_value = QLabel(self.temperature_info_frame)
        self.temperature_value.setObjectName(u"temperature_value")
        self.temperature_value.setGeometry(QRect(10, 72, 82, 30))
        self.temperature_value.setFont(font4)
        self.temperature_value.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.temperature_value.setAlignment(Qt.AlignCenter)
        self.thermometer_picture = QLabel(self.temperature_info_frame)
        self.thermometer_picture.setObjectName(u"thermometer_picture")
        self.thermometer_picture.setGeometry(QRect(0, 0, 101, 121))
        font5 = QFont()
        font5.setFamily(u"MS Serif")
        font5.setPointSize(21)
        self.thermometer_picture.setFont(font5)
        self.thermometer_picture.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.thermometer_picture.setPixmap(QPixmap(u"../../../GUI/Final_Images/term_icon.png"))
        self.thermometer_picture.setAlignment(Qt.AlignCenter)
        self.thermometer_picture.raise_()
        self.temperature_value.raise_()

        self.horizontalLayout_3.addWidget(self.temperature_info_frame)


        self.verticalLayout_2.addWidget(self.temperature_frame_with_buttons_and_info)

        self.pages.addWidget(self.temperature_page)
        self.timer_page = QWidget()
        self.timer_page.setObjectName(u"timer_page")
        self.timer_page.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.timer_frame = QFrame(self.timer_page)
        self.timer_frame.setObjectName(u"timer_frame")
        self.timer_frame.setGeometry(QRect(0, 0, 241, 208))
        self.timer_frame.setMinimumSize(QSize(241, 208))
        self.timer_frame.setMaximumSize(QSize(16777215, 208))
        self.timer_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.timer_frame.setFrameShape(QFrame.StyledPanel)
        self.timer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.timer_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.timer_frame_label = QLabel(self.timer_frame)
        self.timer_frame_label.setObjectName(u"timer_frame_label")
        self.timer_frame_label.setMinimumSize(QSize(221, 33))
        self.timer_frame_label.setMaximumSize(QSize(217, 33))
        self.timer_frame_label.setFont(font)
        self.timer_frame_label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.timer_frame_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.timer_frame_label)

        self.timer_frame_with_buttons_and_info = QFrame(self.timer_frame)
        self.timer_frame_with_buttons_and_info.setObjectName(u"timer_frame_with_buttons_and_info")
        self.timer_frame_with_buttons_and_info.setMinimumSize(QSize(223, 159))
        self.timer_frame_with_buttons_and_info.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.timer_frame_with_buttons_and_info.setFrameShape(QFrame.StyledPanel)
        self.timer_frame_with_buttons_and_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.timer_frame_with_buttons_and_info)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timer_buttons_frame = QFrame(self.timer_frame_with_buttons_and_info)
        self.timer_buttons_frame.setObjectName(u"timer_buttons_frame")
        self.timer_buttons_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.timer_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.timer_buttons_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.timer_buttons_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.timer_plus_button = MyButton(self.timer_buttons_frame)
        self.timer_plus_button.setObjectName(u"timer_plus_button")
        sizePolicy.setHeightForWidth(self.timer_plus_button.sizePolicy().hasHeightForWidth())
        self.timer_plus_button.setSizePolicy(sizePolicy)
        self.timer_plus_button.setMinimumSize(QSize(50, 50))
        self.timer_plus_button.setMaximumSize(QSize(50, 50))
        self.timer_plus_button.setFont(font2)
        self.timer_plus_button.setLayoutDirection(Qt.LeftToRight)
        self.timer_plus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.timer_plus_button.setIconSize(QSize(35, 35))
        self.timer_plus_button.setChecked(False)

        self.gridLayout_5.addWidget(self.timer_plus_button, 0, 0, 1, 1)

        self.timer_minus_button = MyButton(self.timer_buttons_frame)
        self.timer_minus_button.setObjectName(u"timer_minus_button")
        sizePolicy.setHeightForWidth(self.timer_minus_button.sizePolicy().hasHeightForWidth())
        self.timer_minus_button.setSizePolicy(sizePolicy)
        self.timer_minus_button.setMinimumSize(QSize(50, 50))
        self.timer_minus_button.setMaximumSize(QSize(50, 50))
        self.timer_minus_button.setFont(font3)
        self.timer_minus_button.setLayoutDirection(Qt.LeftToRight)
        self.timer_minus_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        self.timer_minus_button.setIconSize(QSize(35, 35))
        self.timer_minus_button.setChecked(False)

        self.gridLayout_5.addWidget(self.timer_minus_button, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.timer_buttons_frame)

        self.timer_info_frame = QFrame(self.timer_frame_with_buttons_and_info)
        self.timer_info_frame.setObjectName(u"timer_info_frame")
        self.timer_info_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.timer_info_frame.setFrameShape(QFrame.StyledPanel)
        self.timer_info_frame.setFrameShadow(QFrame.Raised)
        self.timer_value = QLabel(self.timer_info_frame)
        self.timer_value.setObjectName(u"timer_value")
        self.timer_value.setGeometry(QRect(10, 65, 82, 51))
        self.timer_value.setFont(font4)
        self.timer_value.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.timer_value.setAlignment(Qt.AlignCenter)
        self.sand_wach_picture = QLabel(self.timer_info_frame)
        self.sand_wach_picture.setObjectName(u"sand_wach_picture")
        self.sand_wach_picture.setGeometry(QRect(1, 0, 101, 81))
        self.sand_wach_picture.setFont(font5)
        self.sand_wach_picture.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.sand_wach_picture.setPixmap(QPixmap(u"../../../GUI/Final_Images/sand_clock_icon.png"))
        self.sand_wach_picture.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.timer_info_frame)


        self.verticalLayout_5.addWidget(self.timer_frame_with_buttons_and_info)

        self.pages.addWidget(self.timer_page)
        self.launch_page = QWidget()
        self.launch_page.setObjectName(u"launch_page")
        self.launch_page.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.launch_frame = QFrame(self.launch_page)
        self.launch_frame.setObjectName(u"launch_frame")
        self.launch_frame.setGeometry(QRect(-10, 0, 251, 208))
        self.launch_frame.setMinimumSize(QSize(251, 208))
        self.launch_frame.setMaximumSize(QSize(251, 208))
        self.launch_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.launch_frame.setFrameShape(QFrame.StyledPanel)
        self.launch_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.launch_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.launch_frame_label = QLabel(self.launch_frame)
        self.launch_frame_label.setObjectName(u"launch_frame_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.launch_frame_label.sizePolicy().hasHeightForWidth())
        self.launch_frame_label.setSizePolicy(sizePolicy2)
        self.launch_frame_label.setMinimumSize(QSize(0, 0))
        self.launch_frame_label.setMaximumSize(QSize(16777215, 33))
        self.launch_frame_label.setFont(font)
        self.launch_frame_label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.launch_frame_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.launch_frame_label)

        self.parameters_frame = QFrame(self.launch_frame)
        self.parameters_frame.setObjectName(u"parameters_frame")
        self.parameters_frame.setMinimumSize(QSize(241, 161))
        self.parameters_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.parameters_frame.setFrameShape(QFrame.StyledPanel)
        self.parameters_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.parameters_frame)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, -1, 0, 0)
        self.parameter_file_buttons_frame = QFrame(self.parameters_frame)
        self.parameter_file_buttons_frame.setObjectName(u"parameter_file_buttons_frame")
        self.parameter_file_buttons_frame.setMinimumSize(QSize(61, 0))
        self.parameter_file_buttons_frame.setMaximumSize(QSize(198198, 16777215))
        self.parameter_file_buttons_frame.setLayoutDirection(Qt.LeftToRight)
        self.parameter_file_buttons_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.parameter_file_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.parameter_file_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.parameter_file_buttons_frame)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 6, 0)
        self.load_parameter_file_button = QPushButton(self.parameter_file_buttons_frame)
        self.load_parameter_file_button.setObjectName(u"load_parameter_file_button")
        sizePolicy.setHeightForWidth(self.load_parameter_file_button.sizePolicy().hasHeightForWidth())
        self.load_parameter_file_button.setSizePolicy(sizePolicy)
        self.load_parameter_file_button.setMinimumSize(QSize(0, 0))
        self.load_parameter_file_button.setMaximumSize(QSize(198884, 16777215))
        self.load_parameter_file_button.setLayoutDirection(Qt.LeftToRight)
        self.load_parameter_file_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../../GUI/Final_Images/load_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.load_parameter_file_button.setIcon(icon5)
        self.load_parameter_file_button.setIconSize(QSize(35, 35))
        self.load_parameter_file_button.setChecked(False)

        self.verticalLayout_11.addWidget(self.load_parameter_file_button)

        self.save_parameter_file_button = QPushButton(self.parameter_file_buttons_frame)
        self.save_parameter_file_button.setObjectName(u"save_parameter_file_button")
        sizePolicy.setHeightForWidth(self.save_parameter_file_button.sizePolicy().hasHeightForWidth())
        self.save_parameter_file_button.setSizePolicy(sizePolicy)
        self.save_parameter_file_button.setMinimumSize(QSize(0, 0))
        self.save_parameter_file_button.setLayoutDirection(Qt.LeftToRight)
        self.save_parameter_file_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(62, 93, 143);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../GUI/Final_Images/save_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_parameter_file_button.setIcon(icon6)
        self.save_parameter_file_button.setIconSize(QSize(39, 35))
        self.save_parameter_file_button.setChecked(False)

        self.verticalLayout_11.addWidget(self.save_parameter_file_button)


        self.horizontalLayout.addWidget(self.parameter_file_buttons_frame)

        self.launch_info_frame = QFrame(self.parameters_frame)
        self.launch_info_frame.setObjectName(u"launch_info_frame")
        self.launch_info_frame.setMinimumSize(QSize(0, 161))
        self.launch_info_frame.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.launch_info_frame.setFrameShape(QFrame.StyledPanel)
        self.launch_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.launch_info_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 9)
        self.signal_chosen_label = QLabel(self.launch_info_frame)
        self.signal_chosen_label.setObjectName(u"signal_chosen_label")
        self.signal_chosen_label.setMinimumSize(QSize(160, 0))
        self.signal_chosen_label.setFont(font1)
        self.signal_chosen_label.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.signal_chosen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.signal_chosen_label, 1, 3, 1, 1)

        self.timer_chosen_label = QLabel(self.launch_info_frame)
        self.timer_chosen_label.setObjectName(u"timer_chosen_label")
        self.timer_chosen_label.setMinimumSize(QSize(76, 0))
        self.timer_chosen_label.setFont(font1)
        self.timer_chosen_label.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.timer_chosen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.timer_chosen_label, 3, 0, 1, 1)

        self.temperature_chosen_label = QLabel(self.launch_info_frame)
        self.temperature_chosen_label.setObjectName(u"temperature_chosen_label")
        self.temperature_chosen_label.setMaximumSize(QSize(1568, 16777215))
        self.temperature_chosen_label.setFont(font1)
        self.temperature_chosen_label.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.temperature_chosen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.temperature_chosen_label, 3, 3, 1, 1)

        self.frequyncy_chosen_label = QLabel(self.launch_info_frame)
        self.frequyncy_chosen_label.setObjectName(u"frequyncy_chosen_label")
        self.frequyncy_chosen_label.setFont(font1)
        self.frequyncy_chosen_label.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.frequyncy_chosen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.frequyncy_chosen_label, 2, 3, 1, 1)

        self.power_chosen_label = QLabel(self.launch_info_frame)
        self.power_chosen_label.setObjectName(u"power_chosen_label")
        self.power_chosen_label.setFont(font1)
        self.power_chosen_label.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.power_chosen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.power_chosen_label, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.launch_info_frame)


        self.verticalLayout.addWidget(self.parameters_frame)

        self.launch_status_label = QLabel(self.launch_page)
        self.launch_status_label.setObjectName(u"launch_status_label")
        self.launch_status_label.setGeometry(QRect(0, 200, 171, 39))
        sizePolicy2.setHeightForWidth(self.launch_status_label.sizePolicy().hasHeightForWidth())
        self.launch_status_label.setSizePolicy(sizePolicy2)
        self.launch_status_label.setMinimumSize(QSize(0, 39))
        self.launch_status_label.setMaximumSize(QSize(16777215, 33))
        font6 = QFont()
        font6.setFamily(u"MS Serif")
        font6.setPointSize(16)
        self.launch_status_label.setFont(font6)
        self.launch_status_label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.launch_status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.pages.addWidget(self.launch_page)
        self.sensor_temperature_label = QLabel(self.pages_widget)
        self.sensor_temperature_label.setObjectName(u"sensor_temperature_label")
        self.sensor_temperature_label.setGeometry(QRect(259, 208, 61, 31))
        self.sensor_temperature_label.setFont(font1)
        self.sensor_temperature_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(184, 254, 99);\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.sensor_temperature_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sensor_pressure_label = QLabel(self.pages_widget)
        self.sensor_pressure_label.setObjectName(u"sensor_pressure_label")
        self.sensor_pressure_label.setGeometry(QRect(172, 208, 85, 31))
        self.sensor_pressure_label.setFont(font1)
        self.sensor_pressure_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(99,209,254);\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.sensor_pressure_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.current_countdown_label = QLabel(self.pages_widget)
        self.current_countdown_label.setObjectName(u"current_countdown_label")
        self.current_countdown_label.setGeometry(QRect(87, 208, 83, 31))
        self.current_countdown_label.setFont(font1)
        self.current_countdown_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(254, 228, 166);\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.current_countdown_label.setAlignment(Qt.AlignCenter)
        self.save_file_layout = QFrame(self.pages_widget)
        self.save_file_layout.setObjectName(u"save_file_layout")
        self.save_file_layout.setEnabled(True)
        self.save_file_layout.setGeometry(QRect(10, 0, 320, 240))
        self.save_file_layout.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:reflect, x1:0.559, y1:1, x2:0.548, y2:0, stop:0 rgba(39, 58, 89, 200), stop:1 rgba(27, 39, 65, 200));\n"
"}")
        self.save_file_layout.setFrameShape(QFrame.StyledPanel)
        self.save_file_layout.setFrameShadow(QFrame.Raised)
        self.save_file_frame = QFrame(self.save_file_layout)
        self.save_file_frame.setObjectName(u"save_file_frame")
        self.save_file_frame.setEnabled(True)
        self.save_file_frame.setGeometry(QRect(30, 30, 260, 180))
        self.save_file_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.save_file_frame.setFrameShape(QFrame.StyledPanel)
        self.save_file_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.save_file_frame)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame = QFrame(self.save_file_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 0px solid rgba(0, 0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.save_decor_2 = QLabel(self.frame)
        self.save_decor_2.setObjectName(u"save_decor_2")
        self.save_decor_2.setEnabled(True)
        self.save_decor_2.setMinimumSize(QSize(1, 0))
        self.save_decor_2.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setFamily(u"Tovari Sans")
        font7.setPointSize(50)
        self.save_decor_2.setFont(font7)
        self.save_decor_2.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(99,209,254);\n"
"	border: none\n"
"}\n"
"")
        self.save_decor_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.save_decor_2)

        self.save_file_label = QLabel(self.frame)
        self.save_file_label.setObjectName(u"save_file_label")
        self.save_file_label.setEnabled(True)
        self.save_file_label.setMaximumSize(QSize(174, 16777215))
        font8 = QFont()
        font8.setFamily(u"Tovari Sans")
        font8.setPointSize(18)
        self.save_file_label.setFont(font8)
        self.save_file_label.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	font-size: 18pt;\n"
"	color: rgb(99,209,254);\n"
"	border: none\n"
"}\n"
"")
        self.save_file_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.save_file_label)

        self.save_decor_1 = QLabel(self.frame)
        self.save_decor_1.setObjectName(u"save_decor_1")
        self.save_decor_1.setEnabled(True)
        self.save_decor_1.setMinimumSize(QSize(1, 0))
        self.save_decor_1.setMaximumSize(QSize(123233, 40))
        self.save_decor_1.setFont(font7)
        self.save_decor_1.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	color: rgb(99,209,254);\n"
"	border: none\n"
"}\n"
"")
        self.save_decor_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.save_decor_1)


        self.verticalLayout_13.addWidget(self.frame)

        self.ok_button_save = QPushButton(self.save_file_frame)
        self.ok_button_save.setObjectName(u"ok_button_save")
        self.ok_button_save.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ok_button_save.sizePolicy().hasHeightForWidth())
        self.ok_button_save.setSizePolicy(sizePolicy)
        self.ok_button_save.setMinimumSize(QSize(1, 1))
        self.ok_button_save.setFont(font1)
        self.ok_button_save.setFocusPolicy(Qt.NoFocus)
        self.ok_button_save.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 93, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(84, 126, 193);\n"
"}")
        self.ok_button_save.setIconSize(QSize(0, 45))

        self.verticalLayout_13.addWidget(self.ok_button_save)

        self.load_file_layout = QFrame(self.pages_widget)
        self.load_file_layout.setObjectName(u"load_file_layout")
        self.load_file_layout.setEnabled(True)
        self.load_file_layout.setGeometry(QRect(0, 0, 320, 240))
        self.load_file_layout.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:reflect, x1:0.559, y1:1, x2:0.548, y2:0, stop:0 rgba(39, 58, 89, 200), stop:1 rgba(27, 39, 65, 200));\n"
"}")
        self.load_file_layout.setFrameShape(QFrame.StyledPanel)
        self.load_file_layout.setFrameShadow(QFrame.Raised)
        self.load_file_frame = QFrame(self.load_file_layout)
        self.load_file_frame.setObjectName(u"load_file_frame")
        self.load_file_frame.setEnabled(True)
        self.load_file_frame.setGeometry(QRect(10, 20, 300, 180))
        self.load_file_frame.setLayoutDirection(Qt.RightToLeft)
        self.load_file_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(46, 69, 107);\n"
"	border: 3px solid rgb(62, 93, 143);\n"
"	border-radius: 10px \n"
"}\n"
"")
        self.load_file_frame.setFrameShape(QFrame.StyledPanel)
        self.load_file_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.load_file_frame)
        self.verticalLayout_20.setSpacing(12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.select_load_file_frame = QFrame(self.load_file_frame)
        self.select_load_file_frame.setObjectName(u"select_load_file_frame")
        self.select_load_file_frame.setFocusPolicy(Qt.NoFocus)
        self.select_load_file_frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.select_load_file_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0,0,0,0);\n"
"	border: 0px solid rgba(0,0,0,0)\n"
"}\n"
"")
        self.select_load_file_frame.setFrameShape(QFrame.StyledPanel)
        self.select_load_file_frame.setFrameShadow(QFrame.Raised)
        self.select_load_file_frame.setMidLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.select_load_file_frame)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.next_button = QPushButton(self.select_load_file_frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setMinimumSize(QSize(1, 1))
        font9 = QFont()
        font9.setFamily(u"Tovari Sans")
        font9.setPointSize(20)
        self.next_button.setFont(font9)
        self.next_button.setFocusPolicy(Qt.NoFocus)
        self.next_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 93, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(84, 126, 193);\n"
"}")
        self.next_button.setIconSize(QSize(0, 45))

        self.horizontalLayout_7.addWidget(self.next_button)

        self.load_file_label = QLabel(self.select_load_file_frame)
        self.load_file_label.setObjectName(u"load_file_label")
        self.load_file_label.setEnabled(True)
        self.load_file_label.setMinimumSize(QSize(164, 0))
        self.load_file_label.setMaximumSize(QSize(164, 16777215))
        self.load_file_label.setFont(font8)
        self.load_file_label.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"	font-size: 18pt;\n"
"	color: rgb(232, 238, 119);\n"
"	border: none\n"
"}\n"
"")
        self.load_file_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.load_file_label)

        self.previous_button = MyButton(self.select_load_file_frame)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setEnabled(True)
        sizePolicy.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy)
        self.previous_button.setMinimumSize(QSize(1, 1))
        self.previous_button.setFont(font9)
        self.previous_button.setFocusPolicy(Qt.NoFocus)
        self.previous_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 93, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(84, 126, 193);\n"
"}")
        self.previous_button.setIconSize(QSize(0, 45))

        self.horizontalLayout_7.addWidget(self.previous_button)


        self.verticalLayout_20.addWidget(self.select_load_file_frame)

        self.decor_load_frame = QFrame(self.load_file_frame)
        self.decor_load_frame.setObjectName(u"decor_load_frame")
        self.decor_load_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(0,0,0,0);\n"
"	border: 0px solid rgba(0,0,0,0)\n"
"}\n"
"")
        self.decor_load_frame.setFrameShape(QFrame.StyledPanel)
        self.decor_load_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.decor_load_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.decor_4 = QFrame(self.decor_load_frame)
        self.decor_4.setObjectName(u"decor_4")
        self.decor_4.setMaximumSize(QSize(10, 16777215))
        self.decor_4.setFrameShape(QFrame.StyledPanel)
        self.decor_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.decor_4)

        self.ok_button_load = QPushButton(self.decor_load_frame)
        self.ok_button_load.setObjectName(u"ok_button_load")
        self.ok_button_load.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ok_button_load.sizePolicy().hasHeightForWidth())
        self.ok_button_load.setSizePolicy(sizePolicy)
        self.ok_button_load.setMinimumSize(QSize(1, 1))
        self.ok_button_load.setMaximumSize(QSize(236, 16777215))
        self.ok_button_load.setFont(font1)
        self.ok_button_load.setFocusPolicy(Qt.NoFocus)
        self.ok_button_load.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 93, 143);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(84, 126, 193);\n"
"}")
        self.ok_button_load.setIconSize(QSize(0, 45))

        self.horizontalLayout_9.addWidget(self.ok_button_load)

        self.decor_3 = QFrame(self.decor_load_frame)
        self.decor_3.setObjectName(u"decor_3")
        self.decor_3.setMaximumSize(QSize(10, 16777215))
        self.decor_3.setFrameShape(QFrame.StyledPanel)
        self.decor_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.decor_3)


        self.verticalLayout_20.addWidget(self.decor_load_frame)

        #MainWindow.setCentralWidget(self.pages_widget)
        self.pages.raise_()
        self.menu_frame.raise_()
        self.sensor_temperature_label.raise_()
        self.sensor_pressure_label.raise_()
        self.current_countdown_label.raise_()
        self.save_file_layout.raise_()
        self.load_file_layout.raise_()

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.signal_nav_button.setText("")
        self.frequyncy_and_power_nav_button.setText("")
        self.temperature_nav_button.setText("")
        self.timer_nav_button.setText("")
        self.launch_button.setText("")
        self.signal_frame_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430 \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.signal_button_0.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u044b\u0439", None))
        self.signal_button_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u044b\u0439", None))
        self.signal_button_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043b\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0439", None))
        self.signal_button_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0443\u0441\u043e\u0438\u0434\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.frequyncy_and_power_label.setText(QCoreApplication.translate("MainWindow", u"  \u0427\u0430\u0441\u0442\u043e\u0442\u0430    |  \u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.power_plus_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.power_minus_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.frequyncy_plus_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.frequyncy_minus_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.frequyncy_value.setText(QCoreApplication.translate("MainWindow", u"0 kHz", None))
        self.power_value.setText(QCoreApplication.translate("MainWindow", u"0 %", None))
        self.temperature_frame_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u00b0C", None))
        self.temperature_plus_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.temperature_minus_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.temperature_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.thermometer_picture.setText("")
        self.timer_frame_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440", None))
        self.timer_plus_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.timer_minus_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.timer_value.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.sand_wach_picture.setText("")
        self.launch_frame_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.load_parameter_file_button.setText("")
        self.save_parameter_file_button.setText("")
        self.signal_chosen_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0443\u0441\u043e\u0438\u0434\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.timer_chosen_label.setText(QCoreApplication.translate("MainWindow", u"01:15", None))
        self.temperature_chosen_label.setText(QCoreApplication.translate("MainWindow", u"125 \u00b0C", None))
        self.frequyncy_chosen_label.setText(QCoreApplication.translate("MainWindow", u"100 kHz", None))
        self.power_chosen_label.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.launch_status_label.setText("")
        self.sensor_temperature_label.setText(QCoreApplication.translate("MainWindow", u"125\u00b0C", None))
        self.sensor_pressure_label.setText(QCoreApplication.translate("MainWindow", u"1000 hPa", None))
        self.current_countdown_label.setText(QCoreApplication.translate("MainWindow", u"01:15:00", None))
#if QT_CONFIG(tooltip)
        self.frame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.save_decor_2.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.save_file_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c M-001\n"
"\u0441\u043e\u0445\u0440\u0430\u043d\u0451\u043d", None))
        self.save_decor_1.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.ok_button_save.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.load_file_label.setText(QCoreApplication.translate("MainWindow", u"-------------\n"
"\u0420\u0435\u0436\u0438\u043c M-001\n"
"-------------", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.ok_button_load.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

################################################################################################################################################
################################################################################################################################################
#   При загрузке нового шаблона из QtDesinger в python код, добавить код ниже импортировать билиотеки из прошлой версии, и выполнить несколько действий
#       Кнопки с фрагментом 'us_button = QPushButton(' заменить на 'us_button = MyButton('
#       Кнопки с фрагментом '_nav_button = QPushButton(' заменить на '_nav_button = MyButton(loop = False, parent = '
#       Кнопки с фрагментом 'launch_button = QPushButton(' заменить на 'launch_button = MyButton(loop = False, parent = '
#       Кнопки с регулярным выражением '\d = QPushButton\(' заменить на '\d =MyButton(loop = False, parent = ' заменив \d на оригинальную цифру
#       Строку с фрагментом 'setCentralWidget' закоментировать или удалить вовсе

        self.__set_animation_slide()
        self.hide_save_file_layout()
        self.hide_load_file_layout()

    def hide_save_file_layout(self):
        self.save_file_layout.setEnabled(False)
        self.save_file_layout.setHidden(True)

    def unhide_save_file_layout(self):
        self.save_file_layout.setEnabled(True)
        self.save_file_layout.setHidden(False)

    def set_save_label_text(self, text):
        self.save_file_label.setText(text)

    def hide_load_file_layout(self):
        self.load_file_layout.setEnabled(False)
        self.load_file_layout.setHidden(True)

    def unhide_load_file_layout(self):
        self.load_file_layout.setEnabled(True)
        self.load_file_layout.setHidden(False)

    def set_load_label_text(self, text):
        dash_line = "-" * (len(text)*2-6)
        text = f"{dash_line}\n{text}\n{dash_line}"
        self.load_file_label.setText(text)

    def set_button_state(self, button : MyButton, state : BUTTON_STATE):
        current_geometry = button.getRealGeometry()
        new_geometry = button.getRealGeometry()

        self.set_new_button_size(new_geometry, state.value)
        self.set_button_center_position(new_geometry, current_geometry)

        if(button != self.launch_button):
                button.setStyleSheet(state.value)
        
        button.setRealGeometry(new_geometry)
                
    def set_new_button_size(self, current_geometry: Geometry, size_change : SIZE_CHANGE):
        if size_change == SIZE_CHANGE.UP.value.value:
                current_geometry.width = current_geometry.width*1.1
                current_geometry.height = current_geometry.height*1.2

        elif size_change == SIZE_CHANGE.DOWN.value.value:
                current_geometry.width = current_geometry.width/1.1
                current_geometry.height = current_geometry.height/1.2


    def set_button_center_position(self, new_geometry : Geometry, original_geometry : Geometry):
        new_geometry.x = original_geometry.x-(new_geometry.width-original_geometry.width)/2
        new_geometry.y = original_geometry.y-(new_geometry.height-original_geometry.height)/2

    
    def __set_animation_slide(self):
        self.pages.setTransitionDirection(Qt.Horizontal)
        self.pages.setTransitionSpeed(600) #300 - идеально для windows
        self.pages.setTransitionEasingCurve(QEasingCurve.InOutCubic)
        self.pages.setSlideTransition(True)

    def set_active_page(self, page):
        self.pages.setCurrentWidget(page)

    def update_sensors(self, temperature, pressure):
        self.sensor_temperature_label.setText(temperature)
        self.sensor_pressure_label.setText(pressure)

    def set_launch_button(self, launch_button : LaunchState):   
        self.launch_button.setStyleSheet(launch_button.value)