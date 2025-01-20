#Import pandas with alias
import pandas as pd

# Import dataset as a Pandas dataframe
movies = pd.read_csv('Codecademy\Master_stats_with_Python\L1_variables\movies.csv')

# View the first five rows of the dataframe
print(movies.head())
print(movies.info())

# Print the unique values in the country column
print(movies["country"].value_counts())

# Set the correct value for country_variable_type
country_variable_type = "nominal"

# Set the correct value for release_year_variable_type
release_year_variable_type = "discrete"
print(release_year_variable_type)

# Set the correct value for duration_variable_type
cast_count_variable_type = "discrete"
print(cast_count_variable_type)

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)

# Change the type of the cast_count column
movies['cast_count'].astype("int64")

# Check the data types of the columns again. 
print(movies.dtypes)

# Change the title variable to a "string"
movies['title'] = movies['title'].astype("string")

# Change any other variables
movies['rating'] = movies['rating'].astype("category")

# Print the data types again
print(movies.dtypes)