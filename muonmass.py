# A code to read and sort muon pair mass data from the LHC

#Import libraries

import matplotlib.pylab as pylab
import numpy as np
import scipy
import math
from scipy import stats
from scipy import signal
from scipy import optimize
from scipy.optimize import curve_fit
 #package which finds peaks of data
#Read in data

def read_file(file="upsilons-mass-xaa.txt"):
  data = np.genfromtxt(file) 	#generates list of numbers from the text file
  return data

#Generate Histogram - 6.1

def histogram(data):
    pylab.xlabel('Mass GeV/c^2')
    pylab.ylabel('Frequency')
    pylab.title('A histogram of muon pair mass from LHC data')
    pylab.grid(True)
    xmass = data
    Nbins = 100
    binMin = 8.45
    binMax = 11.0
    counts, binmass, patches = pylab.hist(xmass, bins = Nbins, range = [binMin, binMax])
    # maxima : use builtin function to find (max) peaks
    pylab.savefig("MuonHistogram.pdf")
    pylab.show()
    return counts, binmass

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

'''

#Find the three peaks - 6.2

def find_peaks(counts, mass):
    #Largest peak between between 9.3 - 9.7Gev/c^2
    first_peak = []
    for i in range (0, len(mass)):
        if mass[i] > 9.4 and mass[i] < 9.6:
            if counts[i-1] <= counts[i] >= counts[i+1]:
                first_peak.append(mass[i])
    first_peak_max = np.max(first_peak)
    print("Max mass gamma(1S) is {}".format(np.max(first_peak)))


    second_peak = []
    for i in range (0, len(mass)):
        if mass[i] > 9.9 and mass[i] < 10.2:
            if counts[i-1] <= counts[i] >= counts[i+1]:
                second_peak.append(mass[i])
    second_peak_max = np.max(second_peak)
    print("Max mass gamma(2S) is {}".format(np.max(second_peak)))

    third_peak = []
    for i in range (0, len(mass)):
        if mass[i] > 10.3 and mass[i] < 10.4:
            if counts[i-1] <= counts[i] >= counts[i+1]:
                third_peak.append(mass[i])
    third_peak_max = np.max(third_peak)
    print("Max mass gamma(3S) is {}".format(np.max(third_peak)))

    print("The difference between gamma(1S) and gamma(2S) is {} Gev/c^2.".format(np.max(second_peak) - np.max(first_peak)))
    print("The difference between gamma(1S) and gamma(3S) is {} Gev/c^2.".format(np.max(third_peak) - np.max(first_peak)))
    return first_peak_max

# 6.3

#First peak is from 9.25 to 9.75

def statistics(mass):
    first_peak_area = []
    for i in range (0, len(mass)):
        if mass[i] > 9.25 and mass[i] < 9.75:
            first_peak_area.append(mass[i])
    #print(first_peak_area)
    mean = np.mean(first_peak_area)
    print("The mean of the events in first peak is {} Gev/c^2.".format(np.mean(first_peak_area)))
    variance = np.var(first_peak_area)
    print("The unbiased variance of the events in the first peak is {} Gev/c^2.".format(np.var(first_peak_area)))
    standard_dev = np.std(first_peak_area)
    print("The unbiased standard deviation of the events in the first peak is {} Gev/c^2.".format(np.std(first_peak_area)))
    n = len(first_peak_area)
    standard_dev_of_mean = standard_dev/np.sqrt(n)
    print("The standard deviation on the mean is " + str(standard_dev_of_mean) + " Gev/c^2.")

def FWHM(counts, mass, first_peak_max):
    first_peak_area = []
    for i in range (0, len(mass)):
        if mass[i] > 9.3 and mass[i] < 9.7:
            first_peak_area.append(mass[i])

    heights = []
    for i in range(0, len(mass)):
        if mass[i] > 9.3 and mass[i] < 9.7:
            heights.append(counts[i])
    #print(heights)
    ymax = np.max(heights)
    halfymax = 0.5*ymax
    #print(halfymax)
    masslist = first_peak_area
    #print(first_peak_max)
    peakindex = masslist.index(first_peak_max)
    #print(peakindex)
    greaterthan = True
    lessthan = True
    while greaterthan:
        if heights[peakindex + 1] < halfymax:
            greaterthan = False
            leftwidthindex = peakindex
        peakindex += 1
    peakindex = masslist.index(first_peak_max)
    while lessthan:
        if heights[peakindex - 1] < halfymax:
            lessthan = False
            rightwidthindex = peakindex
        peakindex -= 1
    rightwidth = first_peak_area[rightwidthindex]
    leftwidth = first_peak_area[leftwidthindex]
    width = leftwidth - rightwidth
    #print(rightwidthindex)
    #print(leftwidthindex)
    #print(rightwidth)
    #print(leftwidth)
    print("The FWHM width is " + str(width) + " GeV/c^2")
    #print(first_peak_area)
    #print(heights)
    sigma = len(heights)/(halfymax*(np.sqrt(2*3.14159)))
    print("The mass resolution from the FWHM is " + str(sigma) + " GeV/c^2")

def background_events(mass, counts):
    events = []
    massevents = []
    massband1 = []
    massband2 = []
    for i in range (0, len(mass)):
        if mass[i] > 9.2945 and mass[i] < 9.5945:
            events.append(counts[i])
            number = np.sum(events)
            massevents.append(mass[i])
    print("Number of events N is {}".format(number))
    sideband1 = []
    for i in range (0,len(mass)):
        if mass[i] > 9.1445 and mass[i] < 9.2945:
            sideband1.append(counts[i])
            massband1.append(mass[i])
            number1 = np.sum(sideband1)
    print("Number of events in sideband 1 is {}".format(number1))
    sideband2 = []
    for i in range (0,len(counts)):
        if mass[i] > 9.5945 and mass[i] < 9.7445:
            sideband2.append(counts[i])
            massband2.append(mass[i])
            number2 = np.sum(sideband2)
    print("Number of events in sideband 2 is {}".format(number2))
<<<<<<< HEAD
    #leastsquares = np.linalg.lstsq((np.array(events), np.zeros), (np.array(events), np.zeros))
    #print(leastsquares)

    '''
    Try sideband subtraction
    '''

    k_array = np.divide(massband1, sideband1)
    h_array = np.divide(massband2, sideband2)
    const = (np.mean(k_array) + np.mean(h_array)) * 0.5
    # print(const)
    background = const*np.array(events)
    sum = np.sum(background)
    print("The number of background events are " + str(sum) )
=======
    leastsquares = np.linalg.lstsq(np.array(massevents, 0), np.array(events, 0))
    print(leastsquares)

>>>>>>> 4f222b6389843e713bad2090f016690badaa3e0d

def main():
  data = read_file()
  counts, binmass = histogram(data)
  #histogram_low(data)
  #histogram_mid(data)
  #histogram_high(data)
  peak_mass = find_peaks(counts, binmass)
  statistics(binmass)
  FWHM(counts, binmass, peak_mass)
  noise = background_events(binmass, counts)
main()
