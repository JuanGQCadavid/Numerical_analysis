#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000100]

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5, blocksize=2)

matches = recognize.cheat(samples, newsamples)
x, y = utils.tovalidxy(newsamples, matches)
f = interp1d(x, y, fill_value='extrapolate')
utils.repair(newsamples, matches, f)

import matplotlib.pyplot as plt

plt.title('Linear interpolation')
plt.xlabel('Frame')
plt.ylabel('Amplitude')
plt.plot(samples, label='real')
plt.plot(newsamples, label='interpolated')
plt.legend(loc='best')
plt.show()
