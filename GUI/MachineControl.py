import sys
from PySide2.QtCore import QTimer, QTime, Signal, QObject, QElapsedTimer, QDateTime
from datetime import *
from SignalGenerator import *
from GUI_2_1_2 import Ui_MainWindow
from MachineModel import Model
from Enums import BUTTON_STATE, SignalForm, LaunchState, IndexButtons

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

        self.create_all_handles()
        self.set_values_start_up()

        self.view.signal_nav_button.click()

    def set_values_start_up(self):
        self.model.signal_form.value_change_event.emit()
        self.model.power.value_change_event.emit()
        self.model.frequyncy.value_change_event.emit()
        self.model.timer_param.value_change_event.emit()
        self.model.temperature.value_change_event.emit()

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
        self.model.signal_form.value_change_event.connect(lambda : self.update_signal_form())

        self.model.signal_form.value_change_event.connect(lambda : self.view.signal_chosen_label.setText(self.model.signal_form.get_label_value()))
        self.model.temperature.value_change_event.connect(lambda : self.view.temperature_chosen_label.setText(self.model.temperature.get_label_value()))
        self.model.power.value_change_event.connect(lambda : self.view.power_chosen_label.setText(self.model.power.get_label_value()))
        self.model.frequyncy.value_change_event.connect(lambda : self.view.frequyncy_chosen_label.setText(self.model.frequyncy.get_label_value()))

        self.model.timer_param.value_change_event.connect(lambda : self.view.timer_value.setText(self.model.timer_param.get_label_value()))
        self.model.timer_param.value_change_event.connect(lambda : self.view.timer_chosen_label.setText(self.model.timer_param.get_label_value()))
        self.model.timer_param.value_change_event.connect(lambda : self.view.current_countdown_label.setText(self.model.timer_param.get_label_value() + ":00"))
    
    def create_parameter_ckick_handels(self):
        self.view.signal_button_0.clicked.connect(lambda: self.model.signal_form.set_value(SignalForm.TRIANGLE))
        self.view.signal_button_1.clicked.connect(lambda: self.model.signal_form.set_value(SignalForm.RECTANGULAR))
        self.view.signal_button_2.clicked.connect(lambda: self.model.signal_form.set_value(SignalForm.SAWTOOTH))
        self.view.signal_button_3.clicked.connect(lambda: self.model.signal_form.set_value(SignalForm.SINE))

        self.view.temperature_plus_button.pressed.connect(lambda: self.model.temperature.increment())
        self.view.temperature_minus_button.pressed.connect(lambda: self.model.temperature.dicrement())

        self.view.power_plus_button.pressed.connect(lambda: self.model.power.increment())
        self.view.power_minus_button.pressed.connect(lambda: self.model.power.dicrement())

        self.view.frequyncy_plus_button.pressed.connect(lambda : self.model.frequyncy.increment())
        self.view.frequyncy_minus_button.pressed.connect(lambda : self.model.frequyncy.dicrement())

        self.view.timer_plus_button.pressed.connect(lambda : self.model.timer_param.increment())
        self.view.timer_minus_button.pressed.connect(lambda : self.model.timer_param.dicrement())

        self.view.save_parameter_file_button.clicked.connect(lambda: self.save_mode_window_open())
        self.view.ok_button_save.clicked.connect(lambda: self.save_mode_window_close())

        self.view.load_parameter_file_button.clicked.connect(lambda: self.load_mode_window_open())
        self.view.next_button.clicked.connect(lambda: self.load_mode_window_update(IndexButtons.NEXT))
        self.view.previous_button.clicked.connect(lambda: self.load_mode_window_update(IndexButtons.PREVIOUS))
        self.view.ok_button_load.clicked.connect(lambda: self.load_mode_window_close())

    def create_nav_button_click_enents(self):
        self.view.signal_nav_button.clicked.connect(lambda: self.swicth_page(self.view.signal_page, self.view.signal_nav_button))
        self.view.frequyncy_and_power_nav_button.clicked.connect(lambda: self.swicth_page(self.view.frequyncy_and_power_page, self.view.frequyncy_and_power_nav_button))
        self.view.temperature_nav_button.clicked.connect(lambda: self.swicth_page(self.view.temperature_page, self.view.temperature_nav_button))
        self.view.timer_nav_button.clicked.connect(lambda: self.swicth_page(self.view.timer_page, self.view.timer_nav_button))
        self.view.launch_button.clicked.connect(lambda: self.swicth_page(self.view.launch_page, self.view.launch_button))

    def sensor_tick(self):
        self.view.update_sensors(self.model.temperature_sensor.get_value() + self.model.temperature.unit)

    def update_countdown(self, countdown):
        self.view.current_countdown_label.setText(countdown)

    def tick(self):     
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

    def update_signal_form(self):
        self.view.set_button_state(button=self.model.current_signal_button, state=BUTTON_STATE.INACTIVE)

        if  self.model.signal_form.current_value == SignalForm.TRIANGLE:
            button = self.view.signal_button_0
        elif  self.model.signal_form.current_value == SignalForm.RECTANGULAR:
            button = self.view.signal_button_1
        elif  self.model.signal_form.current_value == SignalForm.SAWTOOTH:
            button = self.view.signal_button_2
        else:
            button = self.view.signal_button_3

        self.model.set_active_signal_button(button)
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
    
    def save_mode_window_open(self):
        text = self.model.save_mode()
        self.view.set_save_label_text(text)
        self.view.unhide_save_file_layout()

    def save_mode_window_close(self):
        self.view.hide_save_file_layout()

    def load_mode_window_open(self):
        self.model.load_mode_list()
        self.load_mode_window_update()
        self.view.unhide_load_file_layout()

    def load_mode_window_update(self, index_button : IndexButtons = None):
        name = None
        if index_button == IndexButtons.NEXT: name = self.model.get_next_mode()
        elif index_button == IndexButtons.PREVIOUS: name = self.model.get_previous_mode()
        else: name = self.model.get_current_mode()
        self.view.set_load_label_text(name)

    def load_mode_window_close(self):
        self.model.load_mode()
        self.view.hide_load_file_layout()
        pass