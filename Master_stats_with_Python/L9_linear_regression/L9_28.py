# training and test sets
# PRMSE - predictive root mean squared error
# Choose the Model with the Lower PRMSE

# Load libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Set seed (don't change this)
np.random.seed(123)

# Import data
bikes = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\bikes.csv')
print(bikes.head())

# Split bikes data
indices = range(len(bikes))
s = int(0.8*len(indices))
train_ind = np.random.choice(indices, size = s, replace = False)
test_ind = list(set(indices) - set(train_ind))
bikes_train = bikes.iloc[train_ind]
bikes_test = bikes.iloc[test_ind]

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + atemp + hum', data=bikes_train).fit()

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ season + windspeed + weekday', data=bikes_train).fit()

# Calculate predicted cnt based on model1
fitted1 = model1.predict(bikes_test)

# Calculate predicted cnt based on model2
fitted2 = model2.predict(bikes_test)

# Calculate PRMSE for model1
true = bikes_test.cnt
prmse1 = np.mean((true-fitted1)**2)**.5

# Calculate PRMSE for model2
prmse2 = np.mean((true-fitted2)**2)**.5

# Print PRMSE for both models
print(f"PRMSE for Model 1: {prmse1}")
print(f"PRMSE for Model 2: {prmse2}")

# Which model performed better based on PRMSE?
which_model = 1 if prmse1 < prmse2 else 2
print(f"The better model based on PRMSE is: Model {which_model}")
