# Histogram project

import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# 
plt.figure(1)
plt.subplot(211)

# Plot the histograms (step 1)
plt.hist(flights, range = (0, 365), bins = 365)
plt.xlabel("Day of the year")
plt.ylabel("Number of flights")
plt.title("Acadia")

#Plot the histograms (step 2)
plt.subplot(212)
plt.hist(in_bloom, range = (0, 365), bins=365)
plt.ylabel("Number of flowers")
plt.xlabel("Day of the year")

plt.tight_layout() # prevent overlapping
plt.show()