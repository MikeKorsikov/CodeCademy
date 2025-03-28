#Inner Merge II


import pandas as pd

sales = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\sales.csv')
print(sales)
targets = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\\targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales,targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
print(crushing_it)

#Inner Merge III
men_women = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\men_women_sales.csv')
print(men_women)

all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
print(results)