from scipy.io import wavfile
import numpy

def wav2points(sample_rate, samples):
    """
    Receives <sample_rate> and <samples> and returns
    two lists <x> and <y>
    """
    samplespersecond = 1.0 / sample_rate
    duration = samplespersecond * len(samples)
    x = numpy.arange(0.0, duration, samplespersecond)
    return x.tolist(), samples.tolist()

def points2wav(x, y):
    """
    Receives <x> and <y> and returns <sample_rate> and <samples>
    * Take care! As conversions are made because of floating point operations.
    * Take double care! As the sample rate can be as hell wrong because of lost points in <x>.
    """
    sample_rate = int(1.0 / (x[1] - x[0]))
    samples = numpy.array(y, dtype=numpy.int16)
    return sample_rate, samples
