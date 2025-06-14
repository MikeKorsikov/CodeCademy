# Correlations

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

# Input code here:
plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4) # has a strong correlation
plt.scatter(df[['min_to_subway']], df[['rent']], alpha=0.4) # has a strong correlation
plt.scatter(df[['floor']], df[['rent']], alpha=0.4) # has a strong correlation

plt.show()