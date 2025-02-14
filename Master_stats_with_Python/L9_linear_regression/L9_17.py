import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


plants = pd.read_csv('Codecademy\\Master_stats_with_Python\\L9_linear_regression\\plants.csv')
model = sm.OLS.from_formula('growth ~ water + fertilizer + water:fertilizer', data=plants).fit()

# Create scatter plot here:
sns.lmplot(x='water', y='growth', hue='fertilizer', palette='Purples', fit_reg=False, data=plants)

# regression lines:
plt.plot(plants.water, model.params[0] + model.params[1]*plants.water+ model.params[2]*2 + model.params[3]*plants.water*2, color='lavender', linewidth=3)
plt.plot(plants.water, model.params[0] + model.params[1]*plants.water+ model.params[2]*4 + model.params[3]*plants.water*4, color='mediumpurple', linewidth=3, label='fertilizer=4')
plt.plot(plants.water, model.params[0] + model.params[1]*plants.water+ model.params[2]*6 + model.params[3]*plants.water*6, color='indigo', linewidth=3, label='fertilizer=6')


# legend:
plt.legend(['fertilizer=2','fertilizer=4','fertilizer=6'])
plt.show()
