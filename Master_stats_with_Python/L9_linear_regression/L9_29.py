# Project on linear regression models

# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Set seed
np.random.seed(1)

# Import data
housing = pd.read_csv('Codecademy\\Master_stats_with_Python\L9_linear_regression\craiglist.csv')
print(housing.head())

# Fit model1
print("\nExercise 1:")
model1 = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths', data=housing).fit()
print(model1.params)

# Fit model2
print("\nExercise 2:")
model2 = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed', data=housing).fit()
print(model2.params)

# Fit model3
print("\nExercise 3:")
model3 = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed + cats_allowed + dogs_allowed', data=housing).fit()
print(model3.params)

# Print R-squared for all models
print("\nExercise 4:")
print(f"Model 1 R-square: {model1.rsquared}") #Output: 0.127 << better explains outcome
print(f"Model 2 R-square: {model2.rsquared}") #Output: 0.281
print(f"Model 3 R-square: {model3.rsquared}") #Output: 0.283


# Print adjusted R-squared for all models
print("\nExercise 5:")
print(f"Model 1 Adj R-square: {model1.rsquared_adj}") #Output: 0.125 << better explains outcome
print(f"Model 2 Adj R-square: {model2.rsquared_adj}") #Output: 0.276
print(f"Model 3 Adj R-square: {model3.rsquared_adj}") #Output: 0.277

# Run an F test comparing model2 and model3
from statsmodels.stats.anova import anova_lm

# Print log likelihood for all models

# Print AIC for all models

# Print BIC for all models

# Split housing data
indices = range(len(housing))
s = int(0.8*len(indices))
train_ind = np.random.choice(indices, size = s, replace = False)
test_ind = list(set(indices) - set(train_ind))
housing_train = housing.iloc[train_ind]
housing_test = housing.iloc[test_ind]

# Fit model2 with training data

# Fit model3 with training data

# Calculate predicted price based on model2

# Calculate predicted price based on model3

# Calculate PRMSE for model2

# Calculate PRMSE for model3

# Print PRMSE for both models