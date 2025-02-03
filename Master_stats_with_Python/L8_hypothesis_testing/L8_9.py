# project - Heart Disease Research Part II

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\heart_disease.csv')

#1
print(heart.head(5))

#2
sns.boxplot(x=heart.heart_disease, y=heart.thalach)
plt.title("Heart disease vs thalach")
plt.show()

#3
thalach_hd = heart[heart["heart_disease"] == "presence"]
thalach_no_hd = heart[heart["heart_disease"] == "absence"]

#4
th_hd_mean = np.mean(thalach_hd['thalach'])
th_no_hd_mean = np.mean(thalach_no_hd['thalach'])
mean_dif = th_hd_mean - th_no_hd_mean
print(f"Mean for present: {th_hd_mean} \nMean for absent: {th_no_hd_mean} \nMean difference: {mean_dif}")

th_hd_median = np.median(thalach_hd['thalach'])
th_no_hd_median = np.median(thalach_no_hd['thalach'])
median_dif = th_hd_median - th_no_hd_median
print(f"\nMedian for present: {th_hd_median} \nMedian for absent: {th_no_hd_median} \nMedian difference: {median_dif}")

#5-6
print("\nExample with 'thalach':")
# Perform independent t-test
tstat, pval = ttest_ind(thalach_hd['thalach'], thalach_no_hd['thalach'])
print(f"P-value: {pval}")
alpha = 0.05  # Significance level
if pval < alpha:
    print("We reject the null hypothesis: There is a significant difference in average thalach between patients with and without heart disease.")
else:
    print("We fail to reject the null hypothesis: No significant difference in average thalach between the groups.")

#7
plt.clf()
sns.boxplot(x=heart.heart_disease, y=heart.chol)
plt.title("Heart disease vs cholesterol")
plt.show()

print("\nExample with 'chol':")
chol_hd = heart[heart["heart_disease"] == "presence"]
chol_no_hd = heart[heart["heart_disease"] == "absence"]
# Perform independent t-test
tstat, pval = ttest_ind(chol_hd['chol'], chol_no_hd['chol'])
print(f"P-value: {pval}")
alpha = 0.05  # Significance level
if pval < alpha:
    print("We reject the null hypothesis: There is a significant difference in average cholesterol between patients with and without heart disease.")
else:
    print("We fail to reject the null hypothesis: No significant difference in average cholesterol between the groups.")

#8
plt.clf()
sns.boxplot(x=heart.cp, y=heart.thalach)
plt.title("Thalach vs type of pain")
plt.show()

#9
print(f"\nTypes of pain: {heart['cp'].unique()}")
thalach_typical = heart[heart["cp"] == "typical angina"]["thalach"]
thalach_asymptom = heart[heart["cp"] == "asymptomatic"]["thalach"]
thalach_nonangin = heart[heart["cp"] == "non-anginal pain"]["thalach"]
thalach_atypical = heart[heart["cp"] == "atypical angina"]["thalach"]

#10
print('\nExercise 10 (ANOVA):')
fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print(f"ANOVA pval: {pval}")
alpha = 0.05  # Significance threshold
if pval < alpha:
    print("We reject the null hypothesis: At least one chest pain type has a significantly different average thalach.")
else:
    print("We fail to reject the null hypothesis: No significant difference in thalach between chest pain types.")

#11
print("\nExercise 11 (Tukey):")
type_I_error_rate =0.05
tukey_results = pairwise_tukeyhsd(heart["thalach"], heart["cp"], type_I_error_rate)
print(tukey_results)

#12
print("\nExercise 12 (crosstab):")
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

#13
print("\nExercise 13 (Chi-Square):")
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)
alpha = 0.05  # Significance level
if pval < alpha:
    print("We reject the null hypothesis: There is a significant association between chest pain type and heart disease diagnosis.")
else:
    print("We fail to reject the null hypothesis: No significant association between chest pain type and heart disease diagnosis.")
