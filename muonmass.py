#A code to read and sort muon pair mass data from the LHC

#Import libraries

import matplotlib.pylab as pylab
import numpy as np
import scipy
from scipy.signal import find_peaks #package which finds peaks of data
#Read in data

def read_file(file="upsilons-mass-xaa.txt"):
  data = np.genfromtxt(file) 	#generates list of numbers from the text file
  return data

#Generate Histogram

def histogram(data):
    pylab.xlabel('Mass GeV/c^2')
    pylab.ylabel('Frequency')
    pylab.title('A histogram of muon pair mass from LHC data')
    pylab.grid(True)
    xmass = data
    Nbins = 50
    binMin = 8.45
    binMax = 11.0
    entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
    pylab.savefig("MuonHistogram.pdf")
    pylab.show()
    #peaks = scipy.signal.find_peaks(, threshold=1500, distance=1)
    #print(peaks)
'''
def findpeaks(data):
    peaks = scipy.signal.find_peaks(data, threshold=1500, distance=1)
    print(peaks)
'''


def histogram_low(data):
    pylab.xlabel('Mass GeV/c^2')
    pylab.ylabel('Frequency')
    pylab.title('A histogram of muon pair mass from LHC data - low')
    pylab.grid(True)
    xmass = data
    Nbins = 50
    binMin = 8.45
    binMax = 9.75
    x = pylab.hist(xmass)
    y = pylab.hist(xmass, bins=50)
    #entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
    #bin_max = np.where(xmass == xmass.max())
    pylab.show()

def histogram_mid(data):
    pylab.xlabel('Mass GeV/c^2')
    pylab.ylabel('Frequency')
    pylab.title('A histogram of muon pair mass from LHC data - mid')
    pylab.grid(True)
    xmass = data
    Nbins = 50
    binMin = 9.75
    binMax = 10.25
    entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
    bin_max = np.where(xmass == xmass.max())
    np.histogram(xmass)

    pylab.show()

def histogram_high(data):
    pylab.xlabel('Mass GeV/c^2')
    pylab.ylabel('Frequency')
    pylab.title('A histogram of muon pair mass from LHC data - high')
    pylab.grid(True)
    xmass = data
    Nbins = 50
    binMin = 10.25
    binMax = 11.0
    entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
    pylab.show()



def main():
  data = read_file()
  histogram(data)
  histogram_low(data)
  histogram_mid(data)
  histogram_high(data)
  #findpeaks(data)

main()
