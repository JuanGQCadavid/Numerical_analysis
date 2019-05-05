#! /usr/bin/env python

import matplotlib.pyplot as plt
from scipy.io import wavfile
from wavmanip import wav2points

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
x, y = wav2points(sample_rate, samples)
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
plt.plot(x, y)
plt.show()
