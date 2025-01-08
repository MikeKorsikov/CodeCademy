# project
# detecting product defects with probability

import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 7

## Task 2:
# how often we might observe the exact expected number of defects (7)
prob = stats.poisson.pmf(lam, lam)
print(prob)

## Task 3:
good_days = stats.poisson.cdf(4, lam)
print(good_days)

## Task 4:
bad_days = 1 - stats.poisson.cdf(9, lam)
print(bad_days)

### Task Group 2 ###
## Task 5:
n_days = 365

#option 1 [np]:
year_defects_1 = np.random.poisson(lam, size = n_days)

#option 2 [stats]:
year_defects = stats.poisson.rvs(lam, size=n_days)

## Task 6:
print(year_defects[0:30])

## Task 7:
days = 365
total_defects_est = days * lam
print(f"Total av defects: {total_defects_est}")

## Task 8:
print(f"Total est defects: {sum(year_defects)}")

## Task 9:
av_est_def = sum(year_defects) / len(year_defects)
print(f"Average from estimate: {round(av_est_def,2)}")

## Task 10:
max_est_def = max(year_defects)
print(f"Max defects per day est: {max_est_def}")

## Task 11:
prob_max = 1 - stats.poisson.cdf(max_est_def - 1, av_est_def)
print(f"Probability of max or more: {round(prob_max*100,2)}%")

### Extra Bonus ###
# Task 12
percentile = 0.9
lambda_param = 7

def_in_90_per = stats.poisson.ppf(percentile, lambda_param)
print(f"Number of defects at 90th percentile: {def_in_90_per}")

# Task 13
