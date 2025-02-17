# Log-Likelihood
# measures the probability of observing our data given a particular model. 
# Higher log-likelihood is better
# A smaller negative number (e.g., -100 vs. -200) is better
# useful when selecting models for prediction

# Load libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Import data
bikes = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + windspeed + holiday', data=bikes).fit()

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ hum + season + weekday', data=bikes).fit()

# Get log-likelihood values
llf_model1 = model1.llf
llf_model2 = model2.llf

# Print log likelihoods
print(f"Model 1 Log-Likelihood: {llf_model1}") # Output -6373 << better
print(f"Model 2 Log-Likelihood: {llf_model2}") # Output: -6390

# Decision logic based on log-likelihood
if llf_model1 > llf_model2:
    which_model = 1
    print("Model 1 is better based on log-likelihood.")
else:
    which_model = 2
    print("Model 2 is better based on log-likelihood.")

# Output the chosen model
print(f"Selected Model: {which_model}")