# Log Transformations
# Algerian Forest Fires project

#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


#load data
forests = pd.read_csv('Codecademy\\Master_stats_with_Python\L9_linear_regression\\forests.csv')
print(forests.head())

#check multicollinearity with a heatmap
print("\nExercise 1:")
corr_grid = forests.select_dtypes(include=['number']).corr()
sns.heatmap(corr_grid, xticklabels=corr_grid.columns, yticklabels=corr_grid.columns, vmin=-1, center=0, vmax=1, cmap='PuOr', annot=True)
plt.title("Heat Map of Correlations")
plt.show()
plt.clf()

#plot humidity vs temperature
print("\nExercise 2:")
sns.lmplot(x="temp" , y="humid", hue="region", data=forests, fit_reg=False)
plt.show()
plt.clf()

#model predicting humidity
print("\nExercise 3:")
modelH = sm.OLS.from_formula('humid ~ temp + region', data=forests).fit()
print(modelH.params)

#equations
print("\nExercise 4:")
print("humid = 142.57 - 2.39 * temp - 7.24 * region")
# humid = 142.57 - 2.39 * temp - 7.24 * region
# Bejaia = 142.57 - 2.39 * temp - 7.24 * 0 OR 142.57 - 2.39 * temp 
# Sidi Bel-abbes = 142.57 - 2.39 * temp - 7.24 * 1 OR 135.33 - 2.39 * temp

#interpretations
print("\nExercise 5:")
## Coefficient on temp: Holding all other variables constant, for every increase of 1 degree Celsius in temperature, humidity decreases by 2.39 percentage points.
## For Bejaia equation: The intercept is 142.57. This is the predicted humidity when the temperature is 0°C and the region is Bejaia
## For Sidi Bel-abbes equation: he intercept is 135.33. This is the predicted humidity when the temperature is 0°C and the region is Sidi Bel-abbes

#plot regression lines
print("\nExercise 6:")
sns.lmplot(x="temp" , y="humid", hue="region", data=forests, fit_reg=False)
# line 1 for Bejaia
plt.plot(forests.temp, modelH.params[0] + modelH.params[2]*forests.temp + modelH.params[1]*0, color="blue", label= "Bejaia")

# line 2 for Sidi Bel-abbes
plt.plot(forests.temp, modelH.params[0] + modelH.params[2]*forests.temp + modelH.params[1]*1, color="orange", label= "Sidi Bel-abbes")

plt.show()
plt.clf()

#plot FFMC vs temperature
print("\nExercise 7:")
sns.lmplot(x="temp" , y="FFMC", hue="fire", data=forests, fit_reg=False)
plt.show()
plt.clf()

#model predicting FFMC with interaction
print("\nExercise 8:")
resultsF = sm.OLS.from_formula('FFMC ~ temp + fire + temp:fire', data=forests).fit()
print(resultsF.params)

#equations
print("\nExercise 9:")
## Full equation:
print("FFMC = -8.1 + 2.44 * temp + 76.78 * fire - 1.88 * temp * fire")
# FFMC = -8.1 + 2.44 * temp + 76.78 * fire - 1.88 * temp:fire

## For locations without fire:
# FFMC = -8.1 + 2.44 * temp

## For locations with fire:
# FFMC = 68.68 + 0.56 * temp

#interpretations
print("\nExercise 10:")
## For locations without fire: for every 1 degree Celsius increase in temperature, FFMC increases by 2.44.

## For locations with fire: for every 1 degree Celsius increase in temperature, FFMC increases by 0.56.


#plot regression lines
print("\nExercise 11:")
sns.lmplot(x="temp" , y="FFMC", hue="fire", data=forests, fit_reg=False)

# line 1 for False (no fire)
plt.plot(forests.temp, resultsF.params[0]+resultsF.params[1]*0+resultsF.params[2]*forests.temp + resultsF.params[3]*forests.temp*0, color='green', label='No Fire')

# line 2 for True (fire)
plt.plot(forests.temp, resultsF.params[0]+resultsF.params[1]*1+resultsF.params[2]*forests.temp + resultsF.params[3]*forests.temp*1, color='red', label='Fire')
plt.legend()
plt.show()
plt.clf()


#plot FFMC vs humid
print("\nExercise 12:")
sns.lmplot(x="humid" , y="FFMC", data=forests, fit_reg=False)
plt.show()
plt.clf()

#polynomial model predicting FFMC
print("\nExercise 13:")
resultsP = sm.OLS.from_formula('FFMC ~ humid + np.power(humid, 2)', data=forests).fit()
print(resultsP.params)

#regression equation
print("\nExercise 14:")
# FFMC = 77.63 + 0.75 * humid - 0.011 * humid ^ 2
print("FFMC = 77.63 + 0.75 * humid - 0.011 * humid ^ 2")

#sample predicted values
h_25 = resultsP.params[0] + resultsP.params[1]*25 + resultsP.params[2]*np.power(25,2)
h_35 = resultsP.params[0] + resultsP.params[1]*35 + resultsP.params[2]*np.power(35,2)
h_60 = resultsP.params[0] + resultsP.params[1]*60 + resultsP.params[2]*np.power(60,2)
h_70 = resultsP.params[0] + resultsP.params[1]*70 + resultsP.params[2]*np.power(70,2)
print(f"{h_25}, \n{h_35}, \n{h_60}, \n{h_70}")

#interpretation of relationship
print("\nExercise 15:")
# There is no linear relationship. Low humidity (dry conditions) leads to high FFMC, but extreme humidity levels lower FFMC

#multiple variables to predict FFMC

#predict FWI from ISI and BUI
print("\nExercise 16:")
modelFFMC = sm.OLS.from_formula('FFMC ~ humid + temp +wind + rain',data=forests).fit()
print(modelFFMC.params)
#predict FWI from ISI and BUI
modelFWI = sm.OLS.from_formula('FWI ~ ISI + BUI',data=forests).fit()
print(modelFWI.params)