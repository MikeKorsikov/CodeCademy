# Tukey's Range Test

from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

# store the data
veryants = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\\veryants.csv')

# run tukey's test
#If you set α = 0.01, you require stronger evidence (only 1% chance of Type I error).
#If you set α = 0.10, you allow more leniency (10% chance of Type I error).

sign_level =0.05
tukey_results = pairwise_tukeyhsd(veryants.Sale, veryants.Store, sign_level)
print(tukey_results)

# determine significance 
a_b_significant = tukey_results.reject[0] # Extract the reject column value
a_c_significant = tukey_results.reject[1]
b_c_significant = tukey_results.reject[2]