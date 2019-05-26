#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils
import matplotlib.pyplot as plt

samplerate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000100]

newsamples = samples.copy()
damage.noiseadd(newsamples, 0.3)
matches = recognize.cheat(samples, newsamples, false_positives=0.04, false_negatives=0.1)
x, y = utils.tovalidxy(newsamples, matches)

flinear = interp1d(x, y, fill_value='extrapolate')
fcubic = interp1d(x, y, kind='cubic', fill_value='extrapolate')

plt.subplot(211)

utils.repair(newsamples, matches, flinear)

plt.title('Linear')
plt.ylabel('Frequency [Hz]')
plt.plot(samples, label='real song')
plt.plot(newsamples, label='interpolated song')

plt.subplot(212)

utils.repair(newsamples, matches, fcubic)

plt.title('Cubic')
plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(samples, label='real song')
plt.plot(newsamples, label='interpolated song')

plt.show()
