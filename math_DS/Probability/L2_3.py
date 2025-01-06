# Probability Mass Function Over a Range using Python

import scipy.stats as stats

# calculating P(2-4 heads) = P(2 heads) + P(3 heads) + P(4 heads) for flipping a coin 10 times
print(stats.binom.pmf(2, n=10, p=.5) + 
      stats.binom.pmf(3, n=10, p=.5) + 
      stats.binom.pmf(4, n=10, p=.5))


# less than or equal to 8
print(1 - (stats.binom.pmf(9, n=10, p=.5) + 
           stats.binom.pmf(10, n=10, p=.5)))


## Checkpoint 1 - probability of observing between 4 to 6 heads from 10 coin flips.
prob_1 = stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5) + stats.binom.pmf(6, n=10, p=.5)
print(prob_1)

## Checkpoint 2 - probability of observing more than 2 heads from 10 coin flips
prob_2 = 1 - (stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5))
print(prob_2)
