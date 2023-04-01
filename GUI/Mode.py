from Enums import SignalForm
import os
from collections import namedtuple

class Mode:
    def __init__(self, 
                temperature : int,
                power : int,
                frequyncy : int,
                timer_param : int,
                signal_form : SignalForm):
        
        self.temperature = temperature
        self.power = power
        self.frequyncy = frequyncy
        self.timer_param = timer_param
        self.signal_form = signal_form

class ModeManager:

    def load_mode_from_file(self, file_path):
        config = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split('=')
                config[key] = value

        return Mode(temperature = int(config['temperature']),
                    power = int(config['power']),
                    frequyncy = int(config['frequyncy']),
                    timer_param = int(config['timer_param']),
                    signal_form = SignalForm(config['signal_form']))

    def save_mode_to_file(self, mode : Mode, file_path = None):
        name = None
        if not file_path:
            name = 'M-{:03d}'.format(len(os.listdir("Modes"))+1)
            file_path = "Modes/" + name + ".mode"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('temperature=' + str(mode.temperature) + '\n')
            f.write('power=' + str(mode.power) + '\n')
            f.write('frequyncy=' + str(mode.frequyncy) + '\n')
            f.write('timer_param=' + str(mode.timer_param) + '\n')
            f.write('signal_form=' + str(mode.signal_form.value))
        return name

    def load_config(self):
        if os.path.isfile('config.mode'):
            return self.load_mode_from_file('config.mode')
        else:
            return self.create_config()

    def update_config(self, mode : Mode):
        self.save_mode_to_file(mode, 'config.mode')
    
    def create_config(self):
        mode = Mode(temperature = 100,
                    power = 10,
                    frequyncy = 5,
                    timer_param = 60,
                    signal_form = SignalForm.SINE)
        self.update_config(mode)
        return mode
    
    def get_mode_list(self):
        directory = "Modes"
        files = os.listdir(directory)
        File = namedtuple('File', ['name', 'full_path'])
        result = []
    def get_mode_list(self):
        directory = "Modes"
        files = os.listdir(directory)
        File = namedtuple('File', ['name', 'full_path'])
        result = []
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == ".mode":
                full_path = os.path.join(directory, file)
                result.append(File(name, full_path))
        return tuple(result)
        return tuple(result)
