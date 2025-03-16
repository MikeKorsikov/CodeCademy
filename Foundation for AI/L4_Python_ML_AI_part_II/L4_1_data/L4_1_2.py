# JSON to CSV
import requests
import csv

# Extract data
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

# Convert to JSON
r_json = r.json()
print(r_json)

# Write to local file
with open('Codecademy/Foundation for AI/L4_Python_ML_AI_part_II/L4_1_data/commute_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(r_json)  # Write the JSON data directly to the CSV file