# Project on linear regression models

# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Set seed
np.random.seed(1)

# Import data
housing = pd.read_csv('craigslist.csv')

# Fit model1

# Fit model2

# Fit model3

# Print R-squared for all models

# Print adjusted R-squared for all models

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