# ANOVA

from scipy.stats import f_oneway, f
import pandas as pd

# store the data
veryants = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\veryants.csv')
a = veryants.Sale[veryants.Store == 'A']
b = veryants.Sale[veryants.Store == 'B']
c = veryants.Sale[veryants.Store == 'C']

# run ANOVA
fstat, pval = f_oneway(a, b, c)

# Print results
print(f"F-statistic: {fstat:.4f}")
print(f"P-value: {pval:.4f}")

# Determine significance
sign_level = 0.05
if pval < sign_level:
    print("ANOVA: There is a statistically significant difference between at least one pair of stores.")
    significant = True
else:
    print("ANOVA: No statistically significant difference was detected among the stores.")
    significant = False

# F-statistic

# Degrees of freedom
df_between = 2  # Number of groups - 1 (3 stores → 3-1=2)
df_within = len(veryants) - 3  # Total samples - Number of groups

# Calculate critical F-value at α = 0.05
f_critical = f.ppf(0.95, df_between, df_within)

# Assess F-statistic magnitude
if fstat < 1:
    print("F-statistic: The variation within groups is higher than the variation between groups, meaning store sales are quite similar.")
elif fstat >= 1 and fstat < f_critical:
    print("F-statistic: There is some between-group variation, but not strong enough to be statistically significant.")
elif fstat >= f_critical:
    print("F-statistic: The variation between stores is large compared to within stores, indicating a meaningful difference in sales.")