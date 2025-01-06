# CDF - Cumulative Distribution Function

# x: the value of interest, looking for the probability of this value or less
# n: the sample size
# p: the probability of success


import scipy.stats as stats

# probability of observing 6 or fewer heads from 10 fair coin flips
print(stats.binom.cdf(6, 10, 0.5))

# probability of observing between 4 and 8 heads from 10 fair coin flips
print(stats.binom.cdf(8, 10, 0.5) - 
      stats.binom.cdf(3, 10, 0.5))

# probability of observing more than 6 heads from 10 fair coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

## Checkpoint 1 - probability of observing 3 or fewer heads
prob_1 = stats.binom.cdf(3, 10, 0.5)
print(prob_1)

# compare to pmf code (checkpoint 2) 
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))


## Checkpoint 3 - probability of observing more than 5 heads
prob_2 = (1 - stats.binom.cdf(5, 10, 0.5))
print(prob_2)


## Checkpoint 4 - probability of observing between 2 and 5 heads
prob_3 = stats.binom.cdf(5, 10, 0.5) - stats.binom.cdf(1, 10, 0.5)
print(prob_3)

# compare to pmf code (checkpoint 5)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))