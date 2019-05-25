#! /usr/bin/env python

from scipy.io import wavfile
import damage, recognize, repair

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)
wavfile.write('songs/zerofill_hakuna_matata', sample_rate, newsamples)

# matches = recognize.kevin(newsamples, max(newsamples) * 0.3)
matches = recognize.cheat(samples, newsamples)

repair.linearinterpolation(newsamples, matches)
wavfile.write('songs/zerofill_kevin_linearinterpolation_hakuna_matata', sample_rate, newsamples)
