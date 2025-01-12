# project

# import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binom_test


# load data
heart = pd.read_csv('Codecademy\math_DS\Inferential_statistics\heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']



# 1
print(f"Exercise 1")
chol_yes_hd = yes_hd.chol
chol_no_hd = no_hd.chol
print(chol_yes_hd)

#2
print("\nExercise 2")
high_chol = 240
mean_chol = np.mean(chol_yes_hd)
print(f"Sample mean: {round(mean_chol,0)}")

#3
print("\nExercise 3")
ttest, two_sided_pval = ttest_1samp(chol_yes_hd, high_chol)
one_sided_pval = round(two_sided_pval / 2,4)
print(f"Two sided pval:{round(two_sided_pval,4)}")

#4
print("\nExercise 4")
print(f"One sided pval:{round(one_sided_pval,4)}")
level_of_sign = 0.05
if one_sided_pval < level_of_sign:
  print("Reject null hypothesis. Pval is significant. (Level is > than average 240)")
else:
  print("Fail to reject.")

  #5
print("\nExercise 5")
ttest, two_sided_pval = ttest_1samp(chol_no_hd, high_chol)
one_sided_pval_no_hd = round(two_sided_pval / 2,4)
print(f"One sided pval:{round(one_sided_pval_no_hd,4)}")

if one_sided_pval_no_hd < level_of_sign:
  print("Reject null hypothesis. Pval is significant. (Level is > than average 240)")
else:
  print("Fail to reject.")

 #6
print("\nExercise 6")
num_patients = len(heart)
print(f"The number of patients: {num_patients}")

 #7
print("\nExercise 7")
fbs_high = 1 # 1 is for > 120 and 0 for < 120 where 1 indicates diabetes
num_highfbs_patients_pd = heart[heart['fbs'] == fbs_high]
num_highfbs_patients = np.sum(heart['fbs'] == fbs_high)
print(f"The number of patients with high level of fbs: {num_highfbs_patients}")

 #8
print("\nExercise 8")
diab_mean = 0.08
num_of_diab = round(diab_mean * num_patients,0)
print(f"Expected number of patients with diabetes: {num_of_diab}")
print(f"Actual number of patients with diabetes: {num_highfbs_patients}")

 #9
print("\nExercise 9")
p_value = binom_test(x=num_highfbs_patients, n=num_patients, p=0.08, alternative='greater')
print(f"P-value is: {p_value}")
 #10
print("\nExercise 10")
significance_threshold = 0.05

if p_value < significance_threshold:
    print("Reject the null hypothesis: The proportion of patients with fbs > 120 mg/dl is significantly greater than 8%.")
else:
    print("Fail to reject the null hypothesis: There is no significant evidence that the proportion of patients with fbs > 120 mg/dl is greater than 8%.")


