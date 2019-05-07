#! /usr/bin/env python

from pointsmanip import *
from scipy.io import wavfile
from wavmanip import *

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

x, y = wav2points(sample_rate, samples)

cutx, cuty = cut(x, y, 0.15)
sample_rate, samples = points2wav(cutx, cuty)
wavfile.write('songs/cut_hakuna_matata.wav', sample_rate, samples)

noisyy = noisy(y, 0.15)
sample_rate, samples = points2wav(x, noisyy)
wavfile.write('songs/noisy_hakuna_matata.wav', sample_rate, samples)
