# Fitting Polynomial Terms in Python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

plants = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\plants.csv')

model = sm.OLS.from_formula('dead ~ light + np.power(light,2)', 
                            data=plants).fit()

print(model.params)

# Compute and save numDead10 and numDead18:
numDead5 = model.params[0] + model.params[1]*5 + model.params[2]*np.power(5,2)
numDead10 = model.params[0] + model.params[1]*10 + model.params[2]*np.power(10,2)
numDead18 = model.params[0] + model.params[1]*18 + model.params[2]*np.power(18,2)

# Print numDead10 and numDead18:
print(numDead5)
print(numDead10)
print(numDead18)


# Interpreting Polynomial Terms
simple = sm.OLS.from_formula('dead ~ light', data=plants).fit()
polynomial = sm.OLS.from_formula('dead ~ light + np.power(light,2)', data=plants).fit()

# Print simple coefficients here:
print(simple.params)

# Print polynomial coefficients here:
print(polynomial.params)

# scatter plot :
sns.lmplot(x='light', y='dead', ci=None, data=plants)
x=np.linspace(0,20,100)
y=polynomial.params[0]+polynomial.params[1]*x+polynomial.params[2]*np.power(x,2)
# polynomial line here:
plt.plot(x, y, linestyle='dashed', linewidth=4, color='black')

# legend and display:
plt.legend(['Simple Model','Polynomial Model'])
plt.show()