# Merge on Specific Columns

import pandas as pd

orders = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\orders.csv')
print(orders)
products = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\products.csv')
print(products)

print("Exercise 1: Merge on Default Columns")
orders_products = pd.merge(
    orders,
    products.rename(columns={'id': 'product_id'}))

print(orders_products)

###
print("\nExercise 2: Merge on Specific Columns")
orders_products = pd.merge(
    orders, # left table
    products, # right table
    left_on='product_id',
    right_on='id',
    suffixes=['_orders', '_products']) # new names of the ID columns

print(orders_products)

###
print("\nExercise 3: Mismatched Merges")

