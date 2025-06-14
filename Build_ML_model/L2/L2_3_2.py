# 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

# create training and testing sets
x = streeteasy[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = streeteasy[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

# checking shapes
print(x_train.shape)
print(x_test.shape)

print(y_train.shape)
print(y_test.shape)

# create a linear regression model
mlr = LinearRegression()

# fit the model to the training data
mlr.fit(x_train, y_train) 

# make predictions on the test data
y_predict = mlr.predict(x_test)


# Test
sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]
predict = mlr.predict(sonny_apartment)
print("Predicted rent: $%.2f" % predict)


# Visualizing Results with Matplotlib

# Create a scatter plot
plt.scatter(y_test, y_predict, alpha=0.4)

# Create x-axis label and y-axis label
plt.xlabel("Actual Rent")
plt.ylabel("Predicted Rent")

# Create a title
plt.title("Actual vs Predicted Rent")

# Show the plot
plt.show()

###
# Print the coefficients of the model
print(mlr.coef_)
