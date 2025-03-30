# project - Page Visits Funnel

import pandas as pd

visits = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\\visits.csv', parse_dates=[1])
cart = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\cart.csv', parse_dates=[1])
checkout = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\checkouts.csv', parse_dates=[1])
purchase = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\purchase.csv', parse_dates=[1])

#1
print("Exercise 1:")
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#2
print("\nExercise 2:")
visits_cart = pd.merge(visits, cart, how='left', on='user_id')

#3
print("\nExercise 3:")
print(len(visits_cart))

#4
print("\nExercise 4:")
null_cart_time = visits_cart[visits_cart.cart_time.isnull()].user_id.count()
print(null_cart_time)

#5
print("\nExercise 5:")
percent_no_cart = float(null_cart_time) / len(visits_cart) * 100
print(f"{percent_no_cart:.2f}%")

#6
print("\nExercise 6:")
cart_checkout = pd.merge(cart, checkout, how='left', on='user_id')
null_checkout = cart_checkout[cart_checkout.checkout_time.isnull()].user_id.count()
percent_no_checkout = float(null_checkout) / len(cart_checkout) * 100
print(f"{percent_no_checkout:.2f}%")

#7
print("\nExercise 7:")
all_data = visits.merge(cart, how='left', on='user_id').merge(checkout, how='left', on='user_id').merge(purchase, how='left', on='user_id')
print(all_data.head())

#8
print("\nExercise 8:")
checkout_purchase = all_data[~all_data.checkout_time.isnull()]
null_purchase = checkout_purchase[checkout_purchase.purchase_time.isnull()].user_id.count()
percent_no_purchase = float(null_purchase) / len(checkout_purchase) * 100
print(f"{percent_no_purchase:.2f}%")

#9


#10
print("\nExercise 10:")
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#11
print("\nExercise 11:")
print(all_data['time_to_purchase'])

#12
print("\nExercise 12:")
avg_time = all_data.time_to_purchase.mean()
print(f"Average time to purchase: {avg_time}")
