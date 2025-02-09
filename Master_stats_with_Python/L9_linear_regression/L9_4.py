# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\\test_data.csv')

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Print the model params
print(results.params)

# Calculate and print `pred_3hr` here:
pred_3hr = results.params[1]*3 + results.params[0]
print(pred_3hr)

#check
pred_3hr_a = 9.848111*3 + 43.016014
print(pred_3hr_a)

# Calculate and print `pred_5hr` here:
newdata = {"hours_studied":[5]}
pred_5hr = results.predict(newdata)
print(pred_5hr)