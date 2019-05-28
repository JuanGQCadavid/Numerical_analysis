#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils, evaluate

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

newsamples = samples.copy()
damage.zerofill(newsamples, 0.05, blocksize=10)
wavfile.write('songs/zerofill_hakuna_matata.wav', sample_rate, newsamples)

matches = recognize.cheat(samples, newsamples)
validx, validy = utils.tovalidxy(newsamples, matches)
f = interp1d(validx, validy, kind='cubic', fill_value='extrapolate')

invalidx = utils.invalidx(matches)
fixedy = f(invalidx)

utils.replace(newsamples, invalidx, fixedy)
wavfile.write('songs/zerofill_cheat_cubic_hakuna_matata.wav', sample_rate, newsamples)

evaluate.study(samples, newsamples, matches=matches)
