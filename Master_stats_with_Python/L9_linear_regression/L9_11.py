# multiple linear regression

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

student = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\student.csv')

# Add code for scatter plot here:
sns.lmplot(x='math1', y='port3', hue='address', fit_reg=False, data=student)
plt.show()

# Fit regression model here:
model1 = sm.OLS.from_formula('port3 ~ math1 + address', data=student).fit()
# Print intercept and coefficients here:
print(model1.params)
print(model1.summary())

# Save intercept and coefficients here:
b0 = model1.params[0] # intercept
b1 = model1.params[2] # math
b2 = model1.params[1] # address
