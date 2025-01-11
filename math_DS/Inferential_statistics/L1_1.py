# T-tests intro
# p-value - probability of observing a test statistic as extreme as, 
# or more extreme than, the one observed, under the assumption that the null hypothesis is true.

# interpretation:
# LOW p-value - Null hypothesis might be wrong and could be rejected (strong evidence against Null)
# HIGH p-value - Null hypothesis is likely to be accurate and valid (weak evidence against Null)

import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt

prices = np.genfromtxt("Codecademy\math_DS\Inferential_statistics\prices.csv")

# Calculate the mean of prices
prices_mean = np.mean(prices)
print("Mean of prices: " + str(prices_mean))

# Perform a one-sample t-test
sample_data = prices
expected_mean = 1000
sign_level = 0.05

tstat, pval = ttest_1samp(sample_data, expected_mean)

# Print the p-value and decision
print(f"p-value: {pval}")
print(f"The p-value as a percentage: {round(pval * 100, 2)}%")

# Decision based on the p-value and significance level
if pval > sign_level:
    print(f"\nConclusion: \nFail to reject the Null hypothesis \n(average cost is not significantly different from {expected_mean}).")
else:
    print(f"\nConclusion: \nReject the Null hypothesis \n(average cost is significantly different from {expected_mean}).")

#plot your histogram here
plt.hist(prices)
plt.show()