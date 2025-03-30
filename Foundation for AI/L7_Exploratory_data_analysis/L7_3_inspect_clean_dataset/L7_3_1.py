#  Inspect, Clean, and Validate a Dataset

# inspect missing data
# isnull() - check for missing values

import pandas as pd
import numpy as np

# code goes here
print("\nExercise 1:")
print("Expected data types:")
print("- Pregnancies: int64")
print("- Glucose: int64")
print("- BloodPressure: int64")
print("- SkinThickness: int64")
print("- Insulin: int64")
print("- BMI: float64")
print("- DiabetesPedigreeFunction: float64")
print("- Age: int64")
print("- Outcome: int64 (binary categorical)")

#
print("\nExercise 2:")
diabetes_data = pd.read_csv('Codecademy\Foundation for AI\L7_Exploratory_data_analysis\L7_3_inspect_clean_dataset\diabetes.csv')
print(diabetes_data.head())

print("\nExercise 3:")
print(f"Number of columns: {len(diabetes_data.columns)}")
print(diabetes_data.columns.tolist())

print("\nExercise 4:")
print(f"Number of rows: {len(diabetes_data)}")

print("\nExercise 5:")
print("Null values in each column:")
print(diabetes_data.isnull().sum())

print("\nExercise 6:")
print(diabetes_data.describe())

print("\nExercise 7:")
print("Oddities in summary statistics:")
print("- Glucose: Min value is 0 (impossible for living patients)")
print("- BloodPressure: Min value is 0 (impossible)")
print("- SkinThickness: Min value is 0 (unlikely for adults)")
print("- Insulin: Min value is 0 (unlikely for all patients)")
print("- BMI: Min value is 0 (impossible)")

print("\nExercise 8:")
print("Other potential outliers:")
print("- Some very high Pregnancy counts (max=17)")
print("- Extreme Insulin values (max=846)")
print("- Very high BMI values (max=67.1)")

print("\nExercise 9:")
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)
print(diabetes_data.describe())

print("\nExercise 10:")
print("Null values after replacement:")
print(diabetes_data.isnull().sum())

print("\nExercise 11:")
print("Rows with missing values:")
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print("\nExercise 12:")
print("Patterns in missing data:")
print("- Many rows missing multiple measurements")
print("- Insulin has the most missing values (374)")
print("- Some patients missing both SkinThickness and Insulin")

print("\nExercise 13:")
print("Data types:")
print(diabetes_data.dtypes)

print("\nExercise 14:")
print("Unique Outcome values:")
print(diabetes_data['Outcome'].unique())

print("\nExercise 15:")
diabetes_data['Outcome'] = pd.to_numeric(diabetes_data['Outcome'], errors='coerce')
diabetes_data['Outcome'] = diabetes_data['Outcome'].fillna(0).astype('int64')
print("After cleaning:")
print(diabetes_data['Outcome'].unique())

print("\nExercise 16:")
print("\nValue counts for key columns:")
for col in ['Pregnancies', 'Glucose', 'Age', 'Outcome']:
    print(f"\n{col}:")
    print(diabetes_data[col].value_counts().sort_index())


