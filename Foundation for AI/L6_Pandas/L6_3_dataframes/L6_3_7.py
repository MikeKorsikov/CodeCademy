# Calculating Aggregate Functions III
import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
cheap_shoes = orders.groupby("shoe_color").price.apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

###

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
print(shoe_counts)

### Reorganizing (pivoting)
# part 1 - groupby
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

# part 2 - pivot
shoe_counts_pivot = shoe_counts.pivot(
  columns='shoe_color',
  index='shoe_type',
  values='id').reset_index()
print(shoe_counts_pivot)

###

user_visits = pd.read_csv('page_visits.csv')

#1
print(user_visits.head())

#2
click_source = user_visits.groupby("utm_source").id.count().reset_index()

#3
print(click_source)

#4
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
print(click_source_by_month)

#5
click_source_by_month_pivot = click_source_by_month.pivot(
  columns='month', # columns
  index='utm_source', # rows
  values='id').reset_index() # values

#6
print(click_source_by_month_pivot)

###

# project 
import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#1
print(ad_clicks.head())

#2
ex2 = ad_clicks.groupby("utm_source").user_id.count().reset_index()
print(ex2)

#3
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

#4
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

#5
clicks_pivot = clicks_by_source.pivot(
  columns='is_click', # columns
  index='utm_source', # rows
  values='user_id').reset_index() # values)
print(clicks_pivot)

#6
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

#7
ex7 = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(ex7) # yes

#8
ex8 = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(ex8)

#9
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']

#10
ex10_a = a_clicks.groupby('day').is_click.sum().reset_index()
ex10_b = b_clicks.groupby('day').is_click.sum().reset_index()
print(ex10_a)
print(ex10_b)

