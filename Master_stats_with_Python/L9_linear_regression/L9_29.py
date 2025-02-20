# Project on linear regression models

# Load libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Set seed
np.random.seed(2)

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
print("\nExercise 6:")
anova_results = anova_lm(model2, model3)
print(anova_results)
p_value = anova_results.at[1, "Pr(>F)"]
print("P-value:", p_value)
significance_threshold = 0.05
which_model = 3 if p_value < significance_threshold else 2
print(f"Selected Model: Model {which_model}") # model 3 is preferred 


# Print log likelihood for all models
print("\nExercise 7:")
llf_model1 = model1.llf
llf_model2 = model2.llf
llf_model3 = model3.llf
print(f"Model 1 Log-Likelihood: {llf_model1}") # Output: -37528
print(f"Model 2 Log-Likelihood: {llf_model2}") # Output: -22989
print(f"Model 3 Log-Likelihood: {llf_model3}") # Output: -22985 << better


# Print AIC for all models
print("\nExercise 8:")
aic_model1 = model1.aic
aic_model2 = model2.aic
aic_model3 = model3.aic
print(f"Model 1 AIC: {aic_model1}") # 75082
print(f"Model 2 AIC: {aic_model2}") # 46029
print(f"Model 3 AIC: {aic_model3}") # 46025 << better

# Print BIC for all models
print("\nExercise 9:")
bic_model1 = model1.bic
bic_model2 = model2.bic
bic_model3 = model3.bic
print(f"Model 1 BIC: {bic_model1}") # 75166
print(f"Model 2 BIC: {bic_model2}") # 46180 << better
print(f"Model 3 BIC: {bic_model3}") # 46188 

# Split housing data
print("\nExercise 10:")
indices = range(len(housing))
s = int(0.8*len(indices))
train_ind = np.random.choice(indices, size = s, replace = False)
test_ind = list(set(indices) - set(train_ind))
housing_train = housing.iloc[train_ind]
housing_test = housing.iloc[test_ind]

# Fit model2 with training data
model2_train = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed', data=housing_train).fit()

# Fit model3 with training data
model3_train = sm.OLS.from_formula('price ~ type + sqfeet + beds + baths + comes_furnished + laundry_options + parking_options + smoking_allowed + cats_allowed + dogs_allowed',data=housing_train).fit()

# Calculate predicted price based on model2
print("\nExercise 11:")
fitted_mod2 = model2_train.predict(housing_test)

# Calculate predicted price based on model3
fitted_mod3 = model3_train.predict(housing_test)

# Calculate PRMSE for model2
true = housing_test["price"]
prmse2 = np.mean((true-fitted_mod2)**2)**.5

# Calculate PRMSE for model3
prmse3 = np.mean((true-fitted_mod3)**2)**.5

# Print PRMSE for both models
print(f"PRMSE for Model 2: {prmse2}") # 410.8 
print(f"PRMSE for Model 3: {prmse3}") # 409.9 << better