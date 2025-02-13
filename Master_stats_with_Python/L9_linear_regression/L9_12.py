# Binary Categorical Variables in Multiple Regression

import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


student = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\student.csv')

model1 = sm.OLS.from_formula('port3 ~ math1 + address', data=student).fit()

# Print model results here:
print(model1.params)

# Save intercepts and slope here:
interceptR = 3.2 # if address == 0 then 3.23 
interceptU = 3.8 # if address == 1 then 3.23 + 0.557?
slope = 0.5 # math coefficient

# Add lines to complete scatter plot and display
sns.lmplot(x='math1', y='port3', hue='address', markers=['o', 'x'], fit_reg=False, data=student)

# Line for rural addresses (R)
plt.plot(student.math1, 3.2+0.5*student.math1, color='blue',linewidth=5)

# Line for urban addresses (U)
plt.plot(student.math1, 3.8+0.5*student.math1, color='orange',linewidth=5)
plt.show()
