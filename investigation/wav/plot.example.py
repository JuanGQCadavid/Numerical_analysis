#! /usr/bin/env python

import matplotlib.pyplot as plt
from scipy.io import wavfile
import damage

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

newsamples = samples.copy()
damage.noiseadd(newsamples, 0.5)

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(samples[1000000:1000100])
plt.plot(newsamples[1000000:1000100])
plt.show()
