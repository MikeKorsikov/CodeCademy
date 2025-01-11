# one-sided p-value
import numpy as np
import pandas as pd

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
observed_value = 41
p_value = np.sum(null_outcomes <= observed_value) / len(null_outcomes)
print (f"P-value is:")
print (p_value)