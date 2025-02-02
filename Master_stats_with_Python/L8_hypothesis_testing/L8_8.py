# Chi-Square Test
# to understand whether the outcomes of two categorical are associated

import pandas as pd
from scipy.stats import chi2_contingency

# read in and print data
ants = pd.read_csv("Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\ants_grade.scv")
print(ants.head())

# create contingency table
table = pd.crosstab(ants.Grade, ants.Ant)
print(table)

# run Chi-Square test and print p-value
chi2, pval, dof, expected = chi2_contingency(table)
print(pval)

# determine significance
# pval < sign level then there is significant association (True)
# pval > sign level then there is no significant association (False)
significant = False