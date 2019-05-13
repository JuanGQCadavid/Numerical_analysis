#! /usr/bin/env python

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import damage, repair

sample_rate, samples = wavfile.read('songs/hakuna_matata.wav')

newsamples = samples.copy()
damage.zerofill(newsamples, 0.5)
wavfile.write('zerofill_hakuna_matata.wav', sample_rate, newsamples)

matches = [y0 == y1 for (y0, y1) in zip(samples, newsamples)]
repair.linearinterpolation(newsamples, matches)
wavfile.write('zerofill_linearinterpolation_hakuna_matata.wav', sample_rate, newsamples)
