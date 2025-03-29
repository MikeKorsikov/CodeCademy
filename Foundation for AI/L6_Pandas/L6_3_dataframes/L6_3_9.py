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
print("\nExercise 3: Outer merge")

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print(store_a_b_outer)

###
print("\nExercise 4: Left merge")
store_a_b_left = pd.merge(store_a, store_b, how="left")
print(store_a_b_left)

store_b_a_left = pd.merge(store_b, store_a, how="left")
print(store_b_a_left)

###
print("\nExercise 5: Concatenate DataFrames")
bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream])
print(menu)