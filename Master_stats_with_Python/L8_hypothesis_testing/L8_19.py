# Familiar: A Study In Data Analysis

# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# Load datasets
lifespans = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\familiar_lifespan.csv')
iron = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\familiar_iron.csv')

# 1
print("\nExercise 1:")
print(lifespans.head())
print(f"\n{iron.head()}")

# 2
print("\nExercise 2:")
vein_pack_lifespans = lifespans[lifespans['pack'] == 'vein']
print(vein_pack_lifespans.head(5))

# 3
print("\nExercise 3:")
vein_lifespan_mean = np.mean(vein_pack_lifespans["lifespan"])
print(vein_lifespan_mean)

# 4
print("\nExercise 4-5:")
average_life_expectancy = 73 # population mean
t_stat, p_value = ttest_1samp(vein_pack_lifespans["lifespan"], average_life_expectancy)

# 5
print(f"P-Value: {p_value}")
if p_value < 0.05:
    print("We reject the null hypothesis: The average lifespan of Vein Pack subscribers is significantly different from 73 years.")
else:
    print("We fail to reject the null hypothesis: There is no significant difference in lifespan from 73 years.")

# 6
print("\nExercise 6:")
artery_pack_lifespans = lifespans[lifespans['pack'] == 'artery']
print(artery_pack_lifespans.head(5))


# 7
print("\nExercise 7:")
artery_lifespan_mean = np.mean(artery_pack_lifespans["lifespan"])
print(artery_lifespan_mean)
v_a_diff = vein_lifespan_mean - artery_lifespan_mean
print(f"Difference between vein and artery is {v_a_diff}")

# 8
print("\nExercise 8-9:")
t_stat, p_value = ttest_ind(vein_pack_lifespans["lifespan"], artery_pack_lifespans["lifespan"])

# 9
print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("We reject the null hypothesis: The average lifespan of Vein Pack subscribers is significantly different from Artery Pack subscribers.")
else:
    print("We fail to reject the null hypothesis: There is no significant difference in lifespan between Vein Pack and Artery Pack subscribers.")


# 10
print("\nExercise 10:")
print(iron.head())

# 11
print("\nExercise 11:")
Xtab = pd.crosstab(iron['pack'], iron['iron'])
print(Xtab)

# 12
print("\nExercise 12-13:")
chi2, pval, dof, expected = chi2_contingency(Xtab)


# 13
print(pval)
if p_value < 0.05:
    print("We reject the null hypothesis: There is a significant association between subscription pack and iron level.")
else:
    print("We fail to reject the null hypothesis: There is no significant association between subscription pack and iron level.")