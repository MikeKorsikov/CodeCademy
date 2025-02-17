# AIC and BIC penalize the log-likelihood for more predictors
# Akaike information criterion (AIC)
# Bayesian information criterion (BIC) << gives bigger penalty 
# we want the model with the LOWEST AIC or BIC

# Load libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Import data
bikes = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + hum + windspeed + season + holiday + weekday', data=bikes).fit()

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ temp + hum + windspeed + season + holiday + weekday + atemp', data=bikes).fit()

# Get model metrics
llf_model1, llf_model2 = model1.llf, model2.llf
aic_model1, aic_model2 = model1.aic, model2.aic
bic_model1, bic_model2 = model1.bic, model2.bic

# Print log-likelihood for both models
print(f"Model 1 Log-Likelihood: {llf_model1}")
print(f"Model 2 Log-Likelihood: {llf_model2}")

# Decision based on log-likelihood (higher is better)
if llf_model1 > llf_model2:
    which_model_loglik = 1
    print("Model 1 is better based on log-likelihood.")
else:
    which_model_loglik = 2
    print("Model 2 is better based on log-likelihood.")

# Print AIC for both models
print(f"\nModel 1 AIC: {aic_model1}")
print(f"Model 2 AIC: {aic_model2}")

# Decision based on AIC (lower is better)
if aic_model1 < aic_model2:
    which_model_aic = 1
    print("Model 1 is better based on AIC.")
else:
    which_model_aic = 2
    print("Model 2 is better based on AIC.")

# Print BIC for both models
print(f"\nModel 1 BIC: {bic_model1}")
print(f"Model 2 BIC: {bic_model2}")

# Decision based on BIC (lower is better)
if bic_model1 < bic_model2:
    which_model_bic = 1
    print("Model 1 is better based on BIC.")
else:
    which_model_bic = 2
    print("Model 2 is better based on BIC.")

# Final output
print(f"\nSelected Model based on Log-Likelihood: Model {which_model_loglik}")
print(f"Selected Model based on AIC: Model {which_model_aic}")
print(f"Selected Model based on BIC: Model {which_model_bic}")