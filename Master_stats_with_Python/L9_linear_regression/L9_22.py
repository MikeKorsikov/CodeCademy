# R-squared
# proportion of variation in an outcome variable 
# that is explained by a linear regression model

# Load libraries
import pandas as pd
import statsmodels.api as sm

# Import data
bikes = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + windspeed + holiday', data=bikes).fit()

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ hum + season + weekday', data=bikes).fit()


# Print R-squared for both models
print(model1.rsquared) #Output: 0.415 << better explains outcome
print(model2.rsquared) #Output: 0.388

# Choose a model
which_model = 1