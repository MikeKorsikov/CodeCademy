#
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])


# Select Rows with Logic I
january  = df[df.month == 'January']
print(january)

# Select Rows with Logic II
march_april = df[(df.month == "March") | (df.month == "April")]
print(march_april) 

# Select Rows with Logic III
january_february_march = df[df.month.isin(['January','February','March'])]
print(january_february_march)

# setting inices
# 1) only old index visible
df2 = df.loc[[1, 3, 5]]
print(df2)

# 2) introduce new but keep old
df3 = df2.reset_index()
print(df3)

# 3) only new index is visible
df2.reset_index(inplace=True, drop=True)
print(df2)
