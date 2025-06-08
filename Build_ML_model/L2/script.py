# project

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print("Exercise 1:")
print(df.head())

print("\nExercise 2:")
prod_per_year = df.groupby('year')['totalprod'].mean().reset_index()
print(prod_per_year.head())

print("\nExercise 3:")
X = prod_per_year['year']
X = X.values.reshape(-1, 1)
print(X[:5]) # Print first 5 elements to check reshaping

print("\nExercise 4:")
y = prod_per_year['totalprod']
print(y.head())

print("\nExercise 5:")
plt.scatter(X, y)
plt.xlabel("Year")
plt.ylabel("Total Honey Production")
plt.title("Total Honey Production per Year")
plt.show()

print("\nExercise 6:")
regr = linear_model.LinearRegression()
print(regr)

print("\nExercise 7:")
regr.fit(X, y)

print("\nExercise 8:")
print("Slope:", regr.coef_[0])
print("Intercept:", regr.intercept_)

print("\nExercise 9:")
y_predict = regr.predict(X)
print(y_predict[:5])

print("\nExercise 10:")
plt.scatter(X, y)
plt.plot(X, y_predict, color='red')
plt.xlabel("Year")
plt.ylabel("Total Honey Production")
plt.title("Total Honey Production per Year with Regression Line")
plt.show()

print("\nExercise 11:")
X_future = np.array(range(2013, 2051))
X_future = X_future.reshape(-1, 1)
print("X_future before reshape (first 5):", np.array(range(2013, 2051))[:5])
print("X_future after reshape (first 5):\n", X_future[:5])

print("\nExercise 12:")
future_predict = regr.predict(X_future)
print(future_predict[:5])

print("\nExercise 13:")
plt.plot(X_future, future_predict)
plt.xlabel("Year")
plt.ylabel("Predicted Honey Production")
plt.title("Predicted Honey Production from 2013 to 2050")
plt.show()

# Get the predicted honey production for the year 2050
honey_2050 = future_predict[-1]
print(f"According to this model, the predicted honey production in the year 2050 will be: {honey_2050:.2f}")