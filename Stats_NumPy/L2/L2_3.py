# Calculating the Mean of 2D Arrays

import numpy as np

ring_toss = np.array([[1, 0, 0], 
                      [0, 0, 1], 
                      [1, 0, 1]])

# for the whole array
print(np.mean(ring_toss))

# for rows
print(np.mean(ring_toss, axis=1))

# for columns
print(np.mean(ring_toss, axis=0))

# Example 2:
allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
# 3 trials (rows)
trial_mean = np.mean(allergy_trials, axis=1)
# 5 patients (columns)
patient_mean = np.mean(allergy_trials, axis=0)

print(total_mean)
print(trial_mean)
print(patient_mean)