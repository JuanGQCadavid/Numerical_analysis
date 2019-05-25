#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)
wavfile.write('songs/zerofill_hakuna_matata.wav', sample_rate, newsamples)

matches = recognize.cheat(samples, newsamples)
validx, validy = utils.tovalidxy(newsamples, matches)
f = interp1d(validx, validy, fill_value='extrapolate')

invalidx = utils.invalidx(matches)
fixedy = f(invalidx)

utils.replace(newsamples, invalidx, fixedy)
wavfile.write('songs/zerofill_cheat_linear_hakuna_matata.wav', sample_rate, newsamples)
