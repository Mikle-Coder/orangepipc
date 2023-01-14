from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd

def generateSineWave(kHz, duration):
    # Задаем частоту сигнала
    frequency = kHz * 1000

    sample_rate = 192000

    # Создаем массив с данными для генерации сигнала
    samples = np.arange(sample_rate * duration) / sample_rate

    # Генерируем сигнал
    signal = np.sin(2 * np.pi * frequency * samples)

    # Воспроизводим сигнал
    print(kHz)
    sd.play(signal, sample_rate)
    sd.wait()


for i in range(2, 82, 2):
    generateSineWave(i, 10)