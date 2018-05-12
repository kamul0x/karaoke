import scikits.audiolab, scipy
#x, fs, nbits = scikits.audiolab.wavread(filename)
#X = scipy.fft(x)
import pylab
Xdb = 20*scipy.log10(scipy.absolute(X))
f = scipy.linspace(0, fs, len(Xdb))
pylab.plot(f, Xdb)
pylab.show()