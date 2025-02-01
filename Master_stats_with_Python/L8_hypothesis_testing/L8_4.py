# Hypothesis Testing: Associations

from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# store the data
veryants = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run t-tests
tstat, a_b_pval = ttest_ind(a, b)
print(f"P-value [a_b]: {round(a_b_pval,4)}")

tstat, a_c_pval = ttest_ind(a, c)
print(f"P-value [a_c]: {round(a_c_pval,4)}")

tstat, b_c_pval = ttest_ind(b, c)
print(f"P-value [b_c]: {round(b_c_pval,4)}")

# determine significance
a_b_significant = a_b_pval < 0.05 
a_c_significant = a_c_pval < 0.05
b_c_significant = b_c_pval < 0.05
print(f"\nA_B significant: {a_b_significant}")
print(f"A_C significant: {a_c_significant}")
print(f"B_C significant: {b_c_significant}")

# create plot
sns.boxplot(data=veryants, x='Store', y='Sale')
plt.show()