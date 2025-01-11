# binomial test

#Purpose: Used to test hypotheses about proportions (success/failure outcomes in binary data).
#Data Type: Binary or categorical data (e.g., "yes/no", "success/failure", "0/1").
#Example Use Case: Testing if the proportion of people who prefer a certain product is equal to 50%.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

monthly_report = pd.read_csv('Codecademy\math_DS\Inferential_statistics\monthly_report.csv')

#print the head of monthly_report:
print(monthly_report.head())

#calculate and print sample_size:
sample_size = (len(monthly_report))
print(f"Total population: {sample_size}")

#calculate and print num_purchased:
num_purchased = (monthly_report["purchase"] == "y").sum()
print(f"Actual n of those who purchased: {num_purchased}")

#simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size=1, p=[0.1, 0.9])

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

#calculate the number of simulated visitors who made a purchase:
num_purchased2  = (simulated_monthly_visitors == "y").sum()
print(f"Number of simulated visitors who made a purchase: {num_purchased2}")

#
null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  num_purchased3 = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased3)

#calculate the minimum and maximum values in null_outcomes here:
null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
print(f"Minimum number: {null_min}")
print(f"Maximum number: {null_max}")

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(num_purchased, color="r")
plt.show()