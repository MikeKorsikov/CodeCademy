# Load libraries
import pandas as pd
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\\test_data.csv')
print(students.head(5))

# Fit the model
model = sm.OLS.from_formula('score ~ hours_studied', students)
results = model.fit()

# Calculate `fitted_values` here:
fitted_values = results.predict(students)
print(fitted_values.head())

# Calculate `residuals` here:
residuals = students.score - fitted_values

# Print the first 5 residuals here:
print(residuals.head(5))
