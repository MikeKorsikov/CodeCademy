import pandas as pd

visits = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\\visits.csv', parse_dates=[1])
checkouts = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\checkouts.csv', parse_dates=[1])

#1
print(visits)
print(checkouts)

#2
v_to_c = pd.merge(visits, checkouts)
print(v_to_c)

#3
v_to_c ['time'] = v_to_c.checkout_time - v_to_c.visit_time
print(v_to_c)

#4
print(v_to_c.time.mean())
