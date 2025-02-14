# Fitting Polynomial Terms in Python
import pandas as pd
import numpy as np
import statsmodels.api as sm

plants = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\plants.csv')

model = sm.OLS.from_formula('dead ~ light + np.power(light,2)', 
                            data=plants).fit()

print(model.params)