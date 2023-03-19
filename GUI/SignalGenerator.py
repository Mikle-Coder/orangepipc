import numpy as np
import sounddevice as sd
import time


class SignalGenerator:
    def __init__(self):
        self.sample_rate = 192000
        self.samples = np.arange(self.sample_rate) / self.sample_rate

    def start(self, signal, frequency):
        frequency = frequency * 1000
        signal = self.__generate(signal, frequency)
        sd.play(signal, self.sample_rate, loop=True)

    def stop(self):
        start = time.time()
        sd.stop()
        end = time.time()
        #print("Stop",str(end - start))

    def __generate(self, signal, frequency):
        return np.sin(2 * np.pi * frequency * self.samples)