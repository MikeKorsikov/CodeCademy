import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\1.csv")
dist_2 = np.genfromtxt("Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\2.csv")

#calculate ratio of standard deviations:
sd1 = np.std(dist_1)
sd2 = np.std(dist_2)
ratio = sd1 / sd2
print(f"sd1 is {sd1} and sd2 is {sd2} so the ratio is {ratio}")

#check normality assumption
normal_assumption = True
print(normal_assumption)

#plot histograms of each distribution
plt.hist(dist_1, alpha = .8, density = True, label = 'dist 1')
plt.hist(dist_2, alpha = .8, density = True, label = 'dist 2')
plt.legend()
plt.show()