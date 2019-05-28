#! /usr/bin/env python

from scipy.io import wavfile
from scipy.interpolate import interp1d
import damage, recognize, utils, evaluate
import numpy as np

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
samples = samples[1000000:2000000]

fp = [0, 0.05, 0.1, 0.2, 0.3]
fn = [0, 0.05, 0.1, 0.2, 0.3]

print('zerofill')
for p in fp:
    for n in fn:
        newsamples = samples.copy()
        damage.zerofill(newsamples, 0.4)
        matches = recognize.cheat(samples, newsamples, false_positives=p, false_negatives=n)
        validx, validy = utils.tovalidxy(newsamples, matches)
        f = interp1d(validx, validy, fill_value='extrapolate')
        invalidx = utils.invalidx(matches)
        fixedy = f(invalidx)
        utils.replace(newsamples, invalidx, fixedy)
        print('fp:', p, 'fn:', n, 'mean:', np.mean(evaluate.abserrors(samples, newsamples)))

print('noiseadd')
for p in fp:
    for n in fn:
        newsamples = samples.copy()
        damage.noiseadd(newsamples, 0.6, rate=0.3)
        matches = recognize.cheat(samples, newsamples, false_positives=p, false_negatives=n)
        validx, validy = utils.tovalidxy(newsamples, matches)
        f = interp1d(validx, validy, fill_value='extrapolate')
        invalidx = utils.invalidx(matches)
        fixedy = f(invalidx)
        utils.replace(newsamples, invalidx, fixedy)
        print('fp:', p, 'fn:', n, 'mean:', np.mean(evaluate.abserrors(samples, newsamples)))
