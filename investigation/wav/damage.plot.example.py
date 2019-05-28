#! /usr/bin/env python

from scipy.io import wavfile
import matplotlib.pyplot as plt
import damage

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[5000000:5000100]

plt.subplot(211)

newsamples = samples.copy()
damage.zerofill(newsamples, 0.3)

plt.title('zeroed vs noisy')
plt.ylabel('Amplitude')
plt.plot(samples, label='real')
plt.plot(newsamples, label='damaged')
plt.legend(loc='best')

plt.subplot(212)

newsamples = samples.copy()
damage.noiseadd(newsamples, 0.7, 0.2)

plt.xlabel('Frame')
plt.ylabel('Amplitude')
plt.plot(samples, label='real')
plt.plot(newsamples, label='damaged')
plt.legend(loc='best')

plt.show()
