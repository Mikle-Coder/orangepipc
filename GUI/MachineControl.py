
import sys
from PySide2.QtCore import QTimer, QTime, Signal, QObject, QElapsedTimer, QDateTime
from datetime import *
from SignalGenerator import *
from GUI_2_1_1 import Ui_MainWindow
from MachineModel import Model
from Enums import BUTTON_STATE, SignalForm, LaunchState

if sys.platform == 'win32':
    from MixerTest import *
    from SensorTest import *
    from HeaterTest import * 
else:
    from Mixer import *
    from Sensor import *
    from Heater import * 

class Control(QObject):
    start_event = Signal()
    pause_event = Signal()
    stop_event = Signal()
    tick_event = Signal()
    sensor_tick_event = Signal()

    def __init__(self, model : Model , view :Ui_MainWindow):
        super(Control, self).__init__()
        self.model = model
        self.view = view

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)
        self.last_triggered_time = QDateTime.currentDateTime()

        self.sensor_timer = QTimer()
        self.sensor_timer.setInterval(500)
        self.sensor_timer.timeout.connect(self.sensor_tick)
        self.sensor_timer.start()

        self.set_values_start_up()
        self.create_all_handles()

        self.view.signal_nav_button.click()
        self.view.signal_button_0.click()

    def set_values_start_up(self):
        self.view.frequyncy_value.setText(self.model.frequyncy.get_label_value())
        self.view.power_value.setText(self.model.power.get_label_value())
        self.view.temperature_value.setText(str(self.model.temperature.current_value))
        self.view.timer_value.setText(self.model.timer_param.get_label_value())
        self.view.timer_chosen_label.setText(self.model.timer_param.get_label_value())
        self.view.temperature_chosen_label.setText(self.model.temperature.get_label_value())
        self.view.frequyncy_chosen_label.setText(self.model.frequyncy.get_label_value())
        self.view.power_chosen_label.setText(self.model.power.get_label_value())
        self.view.current_countdown_label.setText(self.model.timer_param.get_label_value() + ":00")

    def create_all_handles(self):
        self.view.launch_button.holded.connect(lambda : self.handle_launch_button(True))
        self.view.launch_button.clicked.connect(lambda : self.handle_launch_button())
        self.tick_event.connect(lambda : self.tick)

        self.create_change_value_handles()
        self.create_parameter_ckick_handels()
        self.create_nav_button_click_enents()
        
    def create_change_value_handles(self):
        self.model.temperature.value_change_event.connect(lambda : self.view.temperature_value.setText(str(self.model.temperature.current_value)))
        self.model.power.value_change_event.connect(lambda : self.view.power_value.setText(self.model.power.get_label_value()))
        self.model.power.value_change_event.connect(lambda: self.model.mixer.set_volume(self.model.power.current_value))
        self.model.frequyncy.value_change_event.connect(lambda : self.view.frequyncy_value.setText(self.model.frequyncy.get_label_value()))

        self.model.signal_form.value_change_event.connect(lambda : self.view.signal_chosen_label.setText(self.model.signal_form.get_label_value()))
        self.model.temperature.value_change_event.connect(lambda : self.view.temperature_chosen_label.setText(self.model.temperature.get_label_value()))
        self.model.power.value_change_event.connect(lambda : self.view.power_chosen_label.setText(self.model.power.get_label_value()))
        self.model.frequyncy.value_change_event.connect(lambda : self.view.frequyncy_chosen_label.setText(self.model.frequyncy.get_label_value()))

        self.model.timer_param.value_change_event.connect(lambda : self.view.timer_value.setText(self.model.timer_param.get_label_value()))
        self.model.timer_param.value_change_event.connect(lambda : self.view.timer_chosen_label.setText(self.model.timer_param.get_label_value()))
        self.model.timer_param.value_change_event.connect(lambda : self.view.current_countdown_label.setText(self.model.timer_param.get_label_value() + ":00"))
    
    def create_parameter_ckick_handels(self):
        self.view.signal_button_0.clicked.connect(lambda: self.shoose_signal_form(self.view.signal_button_0))
        self.view.signal_button_1.clicked.connect(lambda: self.shoose_signal_form(self.view.signal_button_1))
        self.view.signal_button_2.clicked.connect(lambda: self.shoose_signal_form(self.view.signal_button_2))
        self.view.signal_button_3.clicked.connect(lambda: self.shoose_signal_form(self.view.signal_button_3))

        self.view.temperature_plus_button.pressed.connect(lambda: self.model.temperature.increment())
        self.view.temperature_minus_button.pressed.connect(lambda: self.model.temperature.dicrement())

        self.view.power_plus_button.pressed.connect(lambda: self.model.power.increment())
        self.view.power_minus_button.pressed.connect(lambda: self.model.power.dicrement())

        self.view.frequyncy_plus_button.pressed.connect(lambda : self.model.frequyncy.increment())
        self.view.frequyncy_minus_button.pressed.connect(lambda : self.model.frequyncy.dicrement())

        self.view.timer_plus_button.pressed.connect(lambda : self.model.timer_param.increment())
        self.view.timer_minus_button.pressed.connect(lambda : self.model.timer_param.dicrement())

        self.view.save_parameter_file_button.clicked.connect(lambda: self.save_mode())
        self.view.ok_button.clicked.connect(lambda: self.view.hide_save_file_layout())

    def create_nav_button_click_enents(self):
        self.view.signal_nav_button.clicked.connect(lambda: self.swicth_page(self.view.signal_page, self.view.signal_nav_button))
        self.view.frequyncy_and_power_nav_button.clicked.connect(lambda: self.swicth_page(self.view.frequyncy_and_power_page, self.view.frequyncy_and_power_nav_button))
        self.view.temperature_nav_button.clicked.connect(lambda: self.swicth_page(self.view.temperature_page, self.view.temperature_nav_button))
        self.view.timer_nav_button.clicked.connect(lambda: self.swicth_page(self.view.timer_page, self.view.timer_nav_button))
        self.view.launch_button.clicked.connect(lambda: self.swicth_page(self.view.launch_page, self.view.launch_button))

    def sensor_tick(self):
        ##print("SensorTick")
        self.view.update_sensors(self.model.temperature_sensor.get_value() + self.model.temperature.unit)
        #print("update")

    def update_countdown(self, countdown):
        self.view.current_countdown_label.setText(countdown)

    def tick(self):
        #print("tick")        
        if self.model.timer_duration == 0:
            self.stop()
            self.handle_launch_button(True)
        else:
            self.model.timer_duration = self.model.timer_duration - 1

        hours, remainder = divmod(int(self.model.timer_duration), 3600)
        minutes, seconds = divmod(remainder, 60)
        duration = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        self.update_countdown(duration)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.view.current_countdown_label.setText(self.model.timer_param.get_label_value() + ":00")

    def pause(self):
        self.timer.stop()

    def shoose_signal_form(self, button):
        self.view.set_button_state(button=self.model.current_signal_button, state=BUTTON_STATE.INACTIVE)

        signal_form = None
        if button == self.view.signal_button_0:
            signal_form = SignalForm.TRIANGLE
        elif button == self.view.signal_button_1:
            signal_form = SignalForm.RECTANGULAR
        elif button == self.view.signal_button_2:
            signal_form = SignalForm.SAWTOOTH
        elif button == self.view.signal_button_3:
            signal_form = SignalForm.SINE

        self.model.set_active_signal_form(button, signal_form)
        self.view.set_button_state(button=self.model.current_signal_button, state=BUTTON_STATE.ACTIVE)

    def set_active_page(self, page):
        self.model.set_active_page(page)
        self.view.set_active_page(self.model.current_page)

    def set_active_nav_button(self, button):
        self.view.set_button_state(button=self.model.current_nav_button, state=BUTTON_STATE.INACTIVE)
        self.model.set_active_nav_button(button)
        self.view.set_button_state(button=self.model.current_nav_button, state=BUTTON_STATE.ACTIVE)

    def swicth_page(self, page, button):
        if(self.view.pages.is_sliding or self.model.current_page == page):
                return
        self.set_active_nav_button(button)
        self.set_active_page(page)

    def handle_launch_button(self, hold : bool = False):
        launch_button = self.model.handle_launch_button(hold)
        if launch_button is not None:
            if launch_button == LaunchState.PAUSE:
                self.pause()
            elif launch_button == LaunchState.OFF:
                self.stop()
            elif launch_button == LaunchState.ON:
                self.start()

            self.view.set_launch_button(launch_button)
    
    def save_mode(self):
        self.view.unhide_save_file_layout()
        self.model.save_mode()

    def load_mode():
        pass


            