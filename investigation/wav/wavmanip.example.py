#! /usr/bin/env python

from scipy.io import wavfile
from wavmanip import *

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')
x, y = wav2points(sample_rate, samples)
sample_rate, samples = points2wav(x, y)
wavfile.write('songs/__hakuna_matata.wav', sample_rate, samples)
