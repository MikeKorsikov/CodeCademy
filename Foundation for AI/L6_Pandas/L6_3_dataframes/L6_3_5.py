# project

import codecademylib3
import pandas as pd

#1
inventory = pd.read_csv("inventory.csv")

#2
print(inventory.head(10))

#3
staten_island = inventory.iloc[:10]
print(staten_island)

#4
product_request = staten_island["product_description"]
print(product_request)

#5
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
print(seed_request)

#6
inventory["in_stock"] = inventory.quantity.apply(lambda quantity: True if quantity > 0 else False)
print(inventory.head())

#7
inventory['total_value'] = inventory.apply(lambda row: row["price"] * row["quantity"], axis=1)
print(inventory.head())

#8
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

#9
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)
print(inventory.head())
