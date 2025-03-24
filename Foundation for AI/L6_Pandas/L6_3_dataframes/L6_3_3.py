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
