#project

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('Codecademy\Master_stats_with_Python\L1_variables\census_data.csv', index_col=0)


#1 preview
print(census.head())

#2 check datatypes
print(census.info())

#3
print(census.dtypes)

#4
print(census["birth_year"].unique())

#5
# replace the missing value with 1967
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)

# print out the unique values
print(census['birth_year'].unique())

#6 changing str to int
census['birth_year'] = census['birth_year'].astype('int')
print(census.dtypes)
print(census['birth_year'].unique())

#7 average with np and pd
print(np.mean(census["birth_year"]))
print(census["birth_year"].mean())

#8 add order
census["higher_tax"] = pd.Categorical(census["higher_tax"], ["strongly disagree","disagree", "neutral", "agree",  "strongly agree"], ordered=True)
print(census["higher_tax"].unique())

#9 median
census["higher_tax"] = census["higher_tax"].cat.codes
print(census["higher_tax"].median())

#10 one-hot encode
census = pd.get_dummies(census, columns=["marital_status"])
print(census.head())
