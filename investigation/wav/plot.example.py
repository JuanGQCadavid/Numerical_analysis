#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils
import matplotlib.pyplot as plt

samplerate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000100]

oldsamples = samples.copy()
damage.noiseadd(oldsamples, 0.3)
matches = recognize.cheat(samples, oldsamples)
x, y = utils.tovalidxy(oldsamples, matches)

flinear = interp1d(x, y, fill_value='extrapolate')
fcubic = interp1d(x, y, kind='cubic', fill_value='extrapolate')

newsamples = oldsamples.copy()

plt.subplot(211)

utils.repair(newsamples, matches, flinear)

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(oldsamples)
plt.plot(newsamples)

plt.subplot(212)

utils.repair(newsamples, matches, fcubic)

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(oldsamples)
plt.plot(newsamples)

plt.show()
