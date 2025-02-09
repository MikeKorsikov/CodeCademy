# Categorical Predictors

# Load libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# Read in the data
students = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\\test_data.csv')

# Calculate group means
print(students.groupby('breakfast').mean().score)

# Create the scatter plot here:
plt.scatter(students.breakfast, students.score)

# Add the additional line here:
plt.plot([0,1], [61.66415094339621, 73.7212765957447])

# Show the plot
plt.show()

# Calculate and print group means
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)

# Fit the model and print the coefficients
model = sm.OLS.from_formula('score ~ breakfast', students)
results = model.fit()
print(results.params)

# Calculate and print the difference in group means
mean_difference = mean_score_breakfast - mean_score_no_breakfast
print('Difference in mean scores: ', mean_difference)