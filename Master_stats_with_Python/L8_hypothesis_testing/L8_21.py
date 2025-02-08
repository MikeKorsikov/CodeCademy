# project

# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency , binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\clicks.csv')

#1
print("\nExercise 1:")
print(abdata.head(5))

#2
print("\nExercise 2:")
Xtab = pd.crosstab(abdata['group'], abdata['is_purchase'])
print(Xtab)

#3
print("\nExercise 3:")
chi2_stat, pval, dof, expected = chi2_contingency(Xtab)
print(f"P-Value: {pval}")
if pval < 0.05:
    print("We reject the null hypothesis: There is a significant differece.")
else:
    print("We fail to reject the null hypothesis: No significant difference.")

#4
print("\nExercise 4:")
num_visits = len(abdata)
print(f"Number of visitors: {num_visits}")

#5
print("\nExercise 5:")
num_sales_needed_099 = 1000 / 0.99
print(f"Number of clients at 0.99: {num_sales_needed_099}")

#6
print("\nExercise 6:")
p_sales_needed_099 = num_sales_needed_099 / num_visits
print(f"Proportion of visitors needed for $0.99: {p_sales_needed_099}")

#7
print("\nExercise 7:")
num_sales_needed_199  = 1000 / 1.99
num_sales_needed_499 = 1000 / 4.99
print(f"Number of clients at 1.99: {round(num_sales_needed_199,0)}")
print(f"Number of clients at 4.99: {round(num_sales_needed_499,0)}")

p_sales_needed_199 = num_sales_needed_199 / num_visits
p_sales_needed_499 = num_sales_needed_499 / num_visits
print(f"Proportion of visitors needed for $1.99: {p_sales_needed_199}")
print(f"Proportion of visitors needed for $4.99: {p_sales_needed_499}")

#8
print("\nExercise 8:")
group_A = abdata[abdata['group'] == 'A']

# the number of visitors who were offered the $0.99 price point
samp_size_099 = len(group_A)
print(f"Number which got an offer at 0.99: {samp_size_099}")

# The number of visitors in Group A who made a purchase
sales_099 = group_A[group_A['is_purchase'] == 'Yes'].shape[0]
print(f"Number of people actually purchased: {sales_099}")

#9
print("\nExercise 9:")
group_B = abdata[abdata['group'] == 'B']
group_C = abdata[abdata['group'] == 'C']

samp_size_199 = len(group_B)
sales_199 = group_B[group_B['is_purchase'] == 'Yes'].shape[0]
print(f"Number which got an offer at 1.99: {samp_size_199}")
print(f"Number of people actually purchased: {sales_199}")

samp_size_499 = len(group_C)
sales_499 = group_C[group_C['is_purchase'] == 'Yes'].shape[0]
print(f"Number which got an offer 4.99: {samp_size_499}")
print(f"Number of people actually purchased: {sales_499}")

#10
print("\nExercise 10:")
pvalueA = binom_test(sales_099, samp_size_099, p_sales_needed_099, alternative='greater')
print(f"P-value for A: {pvalueA}")


#11
print("\nExercise 11:")
pvalueB = binom_test(sales_199, samp_size_199, p_sales_needed_199, alternative='greater')
print(f"P-value for B: {pvalueB}")


#12
print("\nExercise 12:")
pvalueC = binom_test(sales_499, samp_size_499, p_sales_needed_499, alternative='greater')
print(f"P-value for C: {pvalueC}")

#13
if pvalueA < 0.05:
    print("Group A ($0.99) is significantly greater than the target.")
else:
    print("Group A ($0.99) is not significantly greater than the target.")

if pvalueB < 0.05:
    print("Group B ($1.99) is significantly greater than the target.")
else:
    print("Group B ($1.99) is not significantly greater than the target.")

if pvalueC < 0.05:
    print("Group C ($4.99) is significantly greater than the target.")
else:
    print("Group C ($4.99) is not significantly greater than the target.")


