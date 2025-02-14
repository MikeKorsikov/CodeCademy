# Matrix Representation of Linear Regression

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

plants = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\plants.csv')

print(plants.head())

# Scatter plot of height and weight here:
sns.lmplot(x="weight" , y="height", hue="species", data=plants, fit_reg=False)
plt.show()
plt.clf()

# Scatter plot of dead and light here:
sns.lmplot(x="light" , y="dead", data=plants, fit_reg=False)
plt.show()

#
# Fit regression model here:
model = sm.OLS.from_formula('height ~ weight + species', data=plants).fit()

# Print coefficients here:
print(model.params)

# Uncomment the scatter plot below:
sns.lmplot(x='weight', y='height', hue='species', markers=['o','x'], fit_reg=False, data=plants)
plt.show()

# form new variable by combining existing two
model1 = sm.OLS.from_formula('height ~ weight + species', data=plants).fit()

# Fit model2 regression here:
model2 = sm.OLS.from_formula('height ~ weight + species + weight:species', data=plants).fit()

# Print model1 results here:
print(model1.params)

# Print model2 results here:
print(model2.params)