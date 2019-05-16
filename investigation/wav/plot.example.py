#! /usr/bin/env python

import matplotlib.pyplot as plt
from scipy.io import wavfile
import damage, repair

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[1000000:1000500]

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)

matches = [y0 == y1 for (y0, y1) in zip(samples, newsamples)]
fixedsamples = newsamples.copy()
repair.linearinterpolation(fixedsamples, matches)

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(samples)
plt.plot(newsamples)
plt.plot(fixedsamples)
plt.show()
