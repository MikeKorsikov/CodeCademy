# PDF - Probability Density Functions
# x: the value of interest
# loc: the mean of the probability distribution
# scale: the standard deviation of the probability distribution


import scipy.stats as stats


# mean of 167.64 cm
# standard deviation of 8 cm

# probability that a randomly chosen woman is less than 158 cm tall
print(stats.norm.cdf(158, 167.64, 8))

# probability that a randomly chosen woman is less than 175 cm tall
prob = stats.norm.cdf(175, 167.64, 8)