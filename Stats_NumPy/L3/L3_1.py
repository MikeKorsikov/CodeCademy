# Statistical distribution
# histogram

import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt 

commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, bins=6, range=(20, 50))
plt.show()