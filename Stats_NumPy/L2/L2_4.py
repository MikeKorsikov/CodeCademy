#Sorting and Outliers

import numpy as np

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps)
print(sorted_temps)

# The median is the middle value of a dataset that’s been 
# ordered in terms of magnitude (from lowest to highest).

large_set = np.genfromtxt('household_income.csv', delimiter=',')

print(large_set)

large_set_median = np.median(large_set)
print(large_set_median)

# 
time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)

minutes_mean = np.mean(time_spent)
print(f"Mean: {minutes_mean}")

minutes_median = np.median(time_spent)
print(f"Median: {minutes_median}")