#A code to read and sort muon pair mass data from the LHC

#Import libraries

import matplotlib.pylab as pylab
import numpy as np
import scipy
from scipy import stats
from scipy import signal
from scipy.signal import argrelextrema, argrelmax #package which finds peaks of data
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
    # maxima : use builtin function to find (max) peaks
    pylab.savefig("MuonHistogram.pdf")
    pylab.show()

def histogram_low(data):
    pylab.xlabel('Mass GeV/c^2')
    pylab.ylabel('Frequency')
    pylab.title('A histogram of muon pair mass from LHC data - low')
    pylab.grid(True)
    xmass = data
    Nbins = 50
    binMin = 8.45
    binMax = 9.75
    entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
    #Largest peak between between 9.3 - 9.7Gev/c^2
    #entries, binedges, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
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

def find_peaks(data):
    #Largest peak between between 9.3 - 9.7Gev/c^2
    first_peak = []
    for i in range (0, len(data)):
        if data[i] > 9.4 and data[i] < 9.5:
            first_peak.append(data[i])
    a = np.histogram(first_peak)
    #print(a)
    b = np.split(a, [1])
    first_peak_max = np.max(b[0])
    first_peak_max_max = np.max(first_peak_max)
    #print(b[0])
    list = first_peak_max.tolist()
    index = list.index(first_peak_max_max)
    #print(first_peak_max)
    #print(first_peak_max_max)
    print(index)
    xmassarray = b[1]
    xmasslist = xmassarray.tolist()
    print(xmasslist)
    X_MASS_THE_CHEEKY_BASTARD = xmasslist[index]
    print(X_MASS_THE_CHEEKY_BASTARD)
    print("Length of first peak list is {}".format(len(first_peak)))
    print("Max mass gamma(1S) is {}".format(np.max(b[0])))
'''
    second_peak = []
    for i in range (0, len(data)):
        if data[i] > 9.9 and data[i] < 10.1:
            second_peak.append(data[i])
    second_peak_max = np.max(second_peak)
    print("Length of second peak list is {}".format(len(second_peak)))
    print("Max mass gamma(2S) is {}".format(np.max(second_peak)))

    third_peak = []
    for i in range (0, len(data)):
        if data[i] > 10.3 and data[i] < 10.4:
            third_peak.append(data[i])
    third_peak_max = np.max(third_peak)
    print("Length of third peak list is {}".format(len(third_peak)))
    print("Max mass gamma(3S) is {}".format(np.max(third_peak)))

    print("The difference between gamma(1S) and gamma(2S) is {}".format(np.max(second_peak) - np.max(first_peak)))
    print("The difference between gamma(1S) and gamma(3S) is {}".format(np.max(third_peak) - np.max(first_peak)))
'''
def main():
  data = read_file()
  histogram(data)
  histogram_low(data)
  histogram_mid(data)
  histogram_high(data)
  find_peaks(data)
main()
