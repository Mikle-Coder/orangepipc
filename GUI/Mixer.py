import alsaaudio

class Mixer():
    def __init__(self):
        self.mix = alsaaudio.Mixer('DAC')
    
    def set_volume(self, volume):
        self.mix.setvolume(volume)
