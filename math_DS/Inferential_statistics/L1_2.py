from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("Codecademy\math_DS\Inferential_statistics\daily_prices.csv", delimiter=",")
print(daily_prices)

# Hypothesis:
# H0 - average price is 1000
# Ha - average price is not 1000

pvals = []

for i in range(10):
  day_1_data = daily_prices[i]
  exp_average = 1000
  ttest, pval = ttest_1samp(day_1_data, exp_average)
  pvals.append(round(pval,2))
  #print(round(pval,2))

print(pvals)

print(f"Smallest p-value: {min(pvals)}")
print(f"Largest p-value: {max(pvals)}")