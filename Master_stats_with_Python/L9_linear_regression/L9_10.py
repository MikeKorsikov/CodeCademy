# project - Linear Regression at Codecademy

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\codecademy.csv')

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(y=codecademy.score, x=codecademy.completed)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data= codecademy)
results = model.fit()
print(results.params)

# Intercept interpretation:
print("If no lessons completed, 13 points will be earned")

# Slope interpretation:
print("for every additional one lesson 1.3 points will be added to score")

# Plot the scatter plot with the line on top
plt.scatter(x=codecademy.completed, y=codecademy.score)
plt.plot(codecademy.completed, results.predict())

# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
newdata = {"completed":[20]}
pred_20 = results.predict(newdata)
print(f"Predicted score: {pred_20[0]}")

# Calculate fitted values
fitted_values = results.predict(codecademy)
print(fitted_values.head(5))

# Calculate residuals
residuals = codecademy.score - fitted_values
print(residuals.head(5))

# Check normality assumption
plt.hist(residuals)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Histogram of Residuals")

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")

# Show then clear the plot
plt.show()
plt.clf()

# Create a boxplot of score vs lesson
sns.boxplot(x= "lesson", y="score", data=codecademy)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', data= codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
print(codecademy.groupby('lesson').mean().score)
lesA = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
lesB = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])
diff_AB = lesA - lesB
print(f"The difference between {lesA} and {lesB} is: {diff_AB}")

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()


