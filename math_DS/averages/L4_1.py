import numpy as np
from scipy import stats

data = [4,6,7,3]
mean_data = np.mean(data)
print(mean_data)

#

data2 = [10,13,7,10,5,15]
mean_data2 = np.mean(data2)
median_data2 = np.median(data2)
mode_data2 = stats.mode(data2)
print(f"Mean: {mean_data2}")
print(f"Median: {median_data2}")
print(f"Mode: {mode_data2}")

#

data3 = [6,8,9,22,90,45,2,22,45,8,22,6,7]
mode_data3 = stats.mode(data3)
print(f"Mode: {mode_data3}")

#

data4 = [15,8,9,15,12,13,2,15,13,8,13,6,7]
mode_data4 = stats.mode(data4)
print(f"Mode: {mode_data4}")

#

data5 = [3,4,1,19,2,1,6]
median_data5 = np.median(data5)
print(f"Mode: {median_data5}")