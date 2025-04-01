import pandas as pd

movies = pd.read_csv('movies.csv')

# Print the first 5 rows 
print(movies.head())

# Print the summary statistics for all columns
print(movies.describe(include='all'))

###

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()
print(mean_budget)

# Save the median to med_budget
med_budget  = movies.production_budget.median()
print(med_budget )

# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()
print(mode_budget)

# Save the trimmed mean to trmean_budget
trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.20)
print(trmean_budget)

###

# Save the range to range_budget
range_budget = movies.production_budget.max() - movies.production_budget.min()
print(f"Range: {range_budget}")

# Save the interquartile range to iqr_budget
iqr_budget = movies.production_budget.quantile(0.75) - movies.production_budget.quantile(0.25)
print(f"IQR range: {iqr_budget}")

# Save the variance to var_budget
var_budget  = movies.production_budget.var()
print(f"Variance: {var_budget}")

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()
print(f"STD: {std_budget}")

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()
print(f"MAD: {mad_budget}")
