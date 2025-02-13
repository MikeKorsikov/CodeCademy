# Quantitative Variables in Multiple Regression

import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


student = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\student.csv')

model2 = sm.OLS.from_formula('port3 ~ math1 + port1', data=student).fit()

# Print resulting coefficients here:
print(model2.params)
print(model2.params[0]) # intercept
print(model2.params[1]) # math
print(model2.params[2]) # portugese

# Scatter plot code:
sns.lmplot(x='math1', y='port3', hue='port1', palette='Blues', fit_reg=False, data=student)

# regression lines
plt.plot(student.math1, model2.params[0]+model2.params[1]*student.math1+model2.params[2]*4, color='lightblue', linewidth=5)
plt.plot(student.math1, model2.params[0]+model2.params[1]*student.math1+model2.params[2]*6, color='blue', linewidth=5)
plt.plot(student.math1, model2.params[0]+model2.params[1]*student.math1+model2.params[2]*8, color='darkblue', linewidth=5)

plt.legend(['score=4','score=6','score=8'])
plt.show()



