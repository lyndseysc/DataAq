#A code to read and sort muon pair mass data from the LHC

#Import libraries

import matplotlib.pylab as pylab
import numpy as np

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

def main():
  data = read_file()
  histogram(data)

main()
