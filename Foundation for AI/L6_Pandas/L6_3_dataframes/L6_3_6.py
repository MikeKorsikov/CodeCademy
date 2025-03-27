# Aggregates in Pandas

import pandas as pd

orders = pd.read_csv('orders.csv')

#1
print(orders.head(10))

#2
most_expensive = orders.price.max()
print(most_expensive)

#3
num_colors = orders.shoe_color.nunique()
print(num_colors)

####

orders = pd.read_csv('orders.csv')
print(orders.head())

#1 most expensive shoe for each shoe_type
pricey_shoes = orders.groupby("shoe_type").price.max()

#2
print(pricey_shoes)

#3
print(type(pricey_shoes))

####

# add reset index
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)

# 
print(type(pricey_shoes))
