#! /usr/bin/env python

import matplotlib.pyplot as plt
from scipy.io import wavfile
import damage

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[1000000:1000500]

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(samples)
plt.plot(newsamples)
plt.show()
