from scipy.io import wavfile
from numpy import arange

def wav2points(sample_rate, samples):
    samplespersecond = 1.0 / sample_rate
    return arange(0.0, samplespersecond * len(samples), samplespersecond), samples

def points2wav(x, y):
    return int(1.0 / (x[1] - x[0])), y
