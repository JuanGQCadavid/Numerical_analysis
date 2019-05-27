#! /usr/bin/env python

from scipy.io import wavfile
from interpolate import NewtonInterpolator
import damage, recognize, utils

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000030]

newsamples = samples.copy()
damage.zerofill(newsamples, 0.3)

matches = recognize.cheat(samples, newsamples)
x, y = utils.tovalidxy(newsamples, matches)
f = NewtonInterpolator(x, y)
utils.repair(newsamples, matches, f)

import matplotlib.pyplot as plt

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(samples)
plt.plot(newsamples)
plt.show()
