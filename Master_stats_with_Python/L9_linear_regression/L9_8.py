# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
website = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\website.csv')

# Print the first five rows
print(website.head())

# 1 Create a scatter plot of time vs age
plt.scatter(website.age, website.time_seconds)
plt.ylabel("Time Spent (seconds)")
plt.xlabel("Age")
plt.title("Scatter Plot of Time Spent vs Age")

# Show then clear plot
plt.show()
plt.clf()

# 2 Fit a linear regression to predict time_seconds based on age
model = sm.OLS.from_formula("time_seconds ~ age", website)
results = model.fit()
print(results.params)

# 3 Plot the scatter plot with the line on top
plt.scatter(website.age, website.time_seconds)
plt.plot(website.age, results.predict())
plt.ylabel("Time Spent (seconds)")
plt.xlabel("Age")
plt.title("Regression Line for Time Spent vs Age")

# Show then clear plot
plt.show()
plt.clf()

# 4 Calculate fitted values
fitted_values = results.predict(website)
print(fitted_values.head(5))

# Calculate residuals
residuals = website.time_seconds - fitted_values
print(residuals.head(5))

# 5 Check normality assumption
plt.hist(residuals)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Histogram of Residuals")

# Show then clear the plot
plt.show()
plt.clf()

# 6 Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")

# Show then clear the plot
plt.show()
plt.clf()

# 7 Predict amount of time on website for 40 year old
newdata = {"age":[40]}
pred_40 = results.predict(newdata)
print(f"Predicted time for 40 yo: {pred_40[0]}")

# 8 Fit a linear regression to predict time_seconds based on the browser
model = sm.OLS.from_formula("time_seconds ~ browser", website)
results = model.fit()
print(results.params)

# 9 Calculate and print the group means (for comparison)
print(website.groupby('browser').mean().time_seconds)
chrome = np.mean(website.time_seconds[website.browser == 'Chrome'])
safari = np.mean(website.time_seconds[website.browser == 'Safari'])
diff_cs = chrome - safari
print(f"The difference between {chrome} and {safari} is: {diff_cs}")
