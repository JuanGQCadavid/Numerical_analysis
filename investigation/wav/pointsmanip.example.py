#! /usr/bin/env python

from pointsmanip import *
from scipy.io import wavfile
from wavmanip import *

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

x, y = wav2points(sample_rate, samples)

noisyy = noisy(y, 0.97)
sample_rate, samples = points2wav(x, noisyy)
wavfile.write('songs/noisy_hakuna_matata.wav', sample_rate, samples)

zerofilledy = zerofilled(y, 0.4)
sample_rate, samples = points2wav(x, zerofilledy)
wavfile.write('songs/zerofilled_hakuna_matata.wav', sample_rate, samples)

invertedy = inverted(y, 0.85)
sample_rate, samples = points2wav(x, invertedy)
wavfile.write('songs/inverted_hakuna_matata.wav', sample_rate, samples)

repeatedy = repeated(y, 0.9)
sample_rate, samples = points2wav(x, repeatedy)
wavfile.write('songs/repeated_hakuna_matata.wav', sample_rate, samples)
