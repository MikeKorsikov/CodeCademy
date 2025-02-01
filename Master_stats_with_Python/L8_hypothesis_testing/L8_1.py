# hypothesis testing
# T-Test

from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("Codecademy\Master_stats_with_Python\L8_hypothesis_testing\daily_prices.csv", delimiter=",")
#print(daily_prices)

# Check the shape to ensure correct indexing
print(daily_prices.shape)

# Hypothesis:
# H0 - average price is 1000
# Ha - average price is not 1000

pvals = []

for i in range(10):
    day_i_data = daily_prices[i, :]  # Assuming daily_prices is a 2D array with days as rows
    exp_average = 1000  # Null hypothesis value
    t_stat, pval = ttest_1samp(day_i_data, exp_average)
    pvals.append(round(pval, 4))  # Rounded to 4 decimal places for better precision

print("P-values for first 10 days:", pvals)
print(f"Smallest p-value: {min(pvals)}")
print(f"Largest p-value: {max(pvals)}")

# Try with a different null hypothesis (e.g., 1050 Rupees)
exp_average_new = 1050
pvals_new = []

for i in range(10):
    day_i_data = daily_prices[i, :]
    t_stat, pval = ttest_1samp(day_i_data, exp_average_new)
    pvals_new.append(round(pval, 4))

print(f"P-values with null hypothesis = {exp_average_new}:", pvals_new)