# FetchMaker

# Import libraries
import numpy as np
import pandas as pd

from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

#1
print("Exercise 1:")
print(dogs.head(5))

#2
print("\nExercise 2:")
pop_mean = 0.08
whippet_rescue = dogs[dogs['breed'] == 'whippet']['is_rescue']
print(whippet_rescue.head(5))

# option 2
whippet_rescue2 = dogs.is_rescue[dogs.breed == 'whippet']
print(whippet_rescue2.head(5))

#3
print("\nExercise 3:")
num_whippet_rescues = whippet_rescue.sum()
print(num_whippet_rescues)

#option 2
num_whippet_rescues2 = np.sum(whippet_rescue == 1)
print(num_whippet_rescues2)

#4
print("\nExercise 4:")
num_whippets = len(whippet_rescue)
print(num_whippets)

#5
print("\nExercise 5:")
pval = binom_test(x=num_whippet_rescues, n=num_whippets, p=pop_mean, alternative='two-sided')
print(pval)
if pval < 0.05:
    print("We reject the null hypothesis: The proportion of whippets who are rescues is significantly different from 8%.")
else:
    print("We fail to reject the null hypothesis: No significant difference from 8%.")

#6
print("\nExercise 6:")
wt_whippets = dogs[dogs['breed'] == 'whippet']['weight']
wt_terriers = dogs[dogs['breed'] == 'terrier']['weight']
wt_pitbulls = dogs[dogs['breed'] == 'pitbull']['weight']

#7
print("\nExercise 7:")
f_stat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls) # ANOVA
print(pval)
if pval < 0.05:
    print("We reject the null hypothesis: At least one pair of dog breeds has significantly different average weights.")
else:
    print("We fail to reject the null hypothesis: No significant difference in average weights among the three breeds.")


#8
print("\nExercise 8:")
tukey_results = pairwise_tukeyhsd(dogs_wtp['weight'], dogs_wtp['breed'], alpha=0.05) # Run Tukey's test
print(tukey_results)

#9
print("\nExercise 9:")
Xtab= pd.crosstab(dogs_ps['color'], dogs_ps['breed'])
print(Xtab)

#10
print("\nExercise 10:")
chi2_stat, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
if pval < 0.05:
    print("We reject the null hypothesis: There is a significant association between breed and color.")
else:
    print("We fail to reject the null hypothesis: No significant association between breed and color.")
