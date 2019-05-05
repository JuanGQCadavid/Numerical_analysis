from scipy.io import wavfile
import numpy

def wav2points(sample_rate, samples):
    samplespersecond = 1.0 / sample_rate
    duration = samplespersecond * len(samples)
    x = numpy.arange(0.0, duration, samplespersecond)
    return x.tolist(), samples.tolist()

def points2wav(x, y):
    sample_rate = int(1.0 / (x[1] - x[0]))
    samples = numpy.array(y, dtype=numpy.int16)
    return sample_rate, samples
