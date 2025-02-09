# Fitting a Linear Regression Model in Python

import pandas as pd
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\\test_data.csv')
print(students.head(5))

# Create the model here:
model = sm.OLS.from_formula('score ~ hours_studied', data = students)

# Fit the model here:
results = model.fit()

# Print the coefficients here:
print(results.params)
