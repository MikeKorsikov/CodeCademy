# PMF - probability mass function
# pmf(x, n, p)
# x: the value of interest
# n: the number of trials
# p: the probability of success


import scipy.stats as stats

# value of interest (probability of observing 3 heads)
# change this
x = 3

# sample size (10 fair coin flips)
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)

## Question 2
prob_2 = stats.binom.pmf(7, 20, 0.5)
print(prob_2)
