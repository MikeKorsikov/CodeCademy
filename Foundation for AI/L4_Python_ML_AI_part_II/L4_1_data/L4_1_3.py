#Exploring data using pandas

import pandas
 
commute_df = pandas.read_csv("Codecademy/Foundation for AI/L4_Python_ML_AI_part_II/L4_1_data/commute_data.csv")

# Preview DataFrame
print(commute_df.head())
 
# Rename DataFrame columns
commute_df.columns = ['county_name', 'total_commuters', 'super_commuters', 'state_code', 'county_code']


print(commute_df.head())