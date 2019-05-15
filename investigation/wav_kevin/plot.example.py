#! /usr/bin/env python

import matplotlib.pyplot as plt
from scipy.io import wavfile
import damage, repair

sample_rate, samples = wavfile.read('songs/hakuna_30_secs.wav')

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)

matches = [y0 == y1 for (y0, y1) in zip(samples, newsamples)]
fixedsamples = newsamples.copy()
repair.linearinterpolation(fixedsamples, matches)

# Detecting maximun change
alpha = 0
x = 0
y_value = 0
for i in range(1,len(samples)):
    delta = abs(samples[i]-samples[i-1])
    if delta > alpha:
        alpha = delta
        x = i
        y_value = samples[i]
print("The maximun change in a song is",alpha,",time:",x,",sample value:",y_value)

plt.xlabel('Frame')
plt.ylabel('Frequency [Hz]')
plt.plot(samples[1000000:1000100])
#plt.plot(newsamples[1000000:1000100])
#plt.plot(fixedsamples[1000000:1000100])
plt.show()
