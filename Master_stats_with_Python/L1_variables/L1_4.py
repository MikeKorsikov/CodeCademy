# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
auto = pd.read_csv('Codecademy/Master_stats_with_Python/L1_variables/autos.csv', index_col=0)

# Print the first 10 rows of the auto dataset 1
print(auto.head(10))

# Print the data types of the auto dataframe 2
print(auto.dtypes)

# Change the data type of price to float 3
auto['price'] = auto['price'].astype("float64")

# Set the engine_size data type to category 4
auto['engine_size'] = pd.Categorical(auto['engine_size'], ['small', 'medium', 'large'], ordered = True)
print(auto['engine_size'].unique())

# Create the engine_codes variable by encoding engine_size 5
auto['engine_size'] = auto['engine_size'].cat.codes
print(auto.head())
print(auto['engine_size'].unique())

# One-Hot Encode the body-style variable 6
auto = pd.get_dummies(auto, columns=["body-style"])
print(auto.head(10))
