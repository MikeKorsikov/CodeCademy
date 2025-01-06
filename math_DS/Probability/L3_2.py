
import scipy.stats as stats

# probability of randomly observing a woman between 165 cm to 175 cm
# P(165 < X < 175) = P(X < 175) - P(X < 165)
# stats.norm.cdf(x, loc, scale) - stats.norm.cdf(x, loc, scale)
print(stats.norm.cdf(175, 167.74, 8) - stats.norm.cdf(165, 167.74, 8))

# probability of observing a woman taller than 172 centimeters
# P(X > 172) = 1 - P(X < 172)
# 1 - stats.norm.cdf(x, loc, scale)
print(1 - stats.norm.cdf(172, 167.74, 8))

## Checkpoint 1
# probability that the weather on a randomly selected day will be between 18 to 25 degrees
#  mean of 20 degrees Celcius and a standard deviation of 3 degrees
temp_prob_1 = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(18, 20, 3)


## Checkpoint 2
# probability that the weather on a randomly selected day will be greater than 24 degrees Celsius
temp_prob_2 = (1 - stats.norm.cdf(24, 20, 3))