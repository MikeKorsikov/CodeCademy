#
import pandas as pd

# dimensions
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

# columns
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115],
],
  columns=['Store ID', 'Location', 'Number of Employees'])

print(df2)

# loading from CSV into DF
df3 = pd.read_csv('sample.csv')

# saving to CSV file
df4.to_csv('new-csv-file.csv')

# inspecting DF
df5 = pd.read_csv('imdb.csv')
print(df5.head()) # to see first 5 rows
print(df5.info()) # to see metadata (dtypes)

#
