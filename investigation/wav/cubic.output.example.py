#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[1000000:1000000 + 10 * sample_rate] # only 10s as it takes way too long

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)
wavfile.write('songs/zerofill_hakuna_matata.wav', sample_rate, newsamples)

matches = recognize.cheat(samples, newsamples)
x, y = utils.tovalidxy(newsamples, matches)
f = interp1d(x, y, kind='cubic', fill_value='extrapolate')

utils.repair(newsamples, matches, f)
wavfile.write('songs/zerofill_cheat_cubic_hakuna_matata.wav', sample_rate, newsamples)
