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
           'clinic_west']
)

# selecting column
clinic_north = df['clinic_north']

# checking data type
print(type(clinic_north)) # <class 'pandas.core.series.Series'>

# checking data type
print(type(df)) # <class 'pandas.core.frame.DataFrame'>

# select row
march = df.iloc[2]  # second row in the df
print(march)

# select multiple rows
april_may_june = df.iloc[3:6]
print(april_may_june)
