#! /usr/bin/env python
from scipy.io import wavfile
import damage, repair

sample_rate, samples = wavfile.read('songs/hakuna_30_secs.wav')

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)
wavfile.write('damaged_songs/zerofill_hakuna_30secs.wav', sample_rate, newsamples)
n = len(newsamples)
print(n)
x_to_interpolate = repair.damage_recognition(n, newsamples, 8400)
matches = [y0 == y1 for (y0, y1) in zip(samples, newsamples)]

for i in range(len(matches)):
    if x_to_interpolate[i] != matches[i]:
        print("Error at: ", i)
        print("x[i] vs matches[i]")
        print(x_to_interpolate[i], "vs", matches[i])
        print(samples[i],"vs",newsamples[i])
#print(matches)
#repair.linearinterpolation(newsamples, matches)
#wavfile.write('repaired_songs/zerofill_linearinterpolation_hakuna_30_secs.wav', sample_rate, newsamples)
