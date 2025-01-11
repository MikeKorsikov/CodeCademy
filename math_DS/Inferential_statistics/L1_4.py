import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the 90% interval here:
null_90CI = np.percentile(null_outcomes, [5, 95])
print("90% Confidence Interval:", null_90CI)

# Check if the observed value is inside the interval
observed_value = 41
if null_90CI[0] <= observed_value <= null_90CI[1]:
    print(f"The observed value {observed_value} is inside the 90% confidence interval.")
else:
    print(f"The observed value {observed_value} is outside the 90% confidence interval.")