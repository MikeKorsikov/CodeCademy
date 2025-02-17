# F-Test
# 1. H0 - Additional predictors do NOT improve model
# 2. HA - at least one predictor significantly improves model
# 3. F-statistics measures how much additional predictors improve model
# 4. Higher F-statistic explains more
# 5. If p-value < 0.05 - reject H0



# Load libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Import data
bikes = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\bikes.csv')

# Fit model1
model1 = sm.OLS.from_formula('cnt ~ temp + hum + windspeed', data=bikes).fit()

# Fit model2
model2 = sm.OLS.from_formula('cnt ~ temp + hum + windspeed + weekday + atemp', data=bikes).fit()

# Run the F-test and print results
anova_results = anova_lm(model1, model2)
print(anova_results)

p_value = anova_results.at[1, "Pr(>F)"]
print("P-value:", p_value)

# Choose the better model based on p-value
significance_threshold = 0.05
which_model = 2 if p_value < significance_threshold else 1

print(f"Selected Model: Model {which_model}")