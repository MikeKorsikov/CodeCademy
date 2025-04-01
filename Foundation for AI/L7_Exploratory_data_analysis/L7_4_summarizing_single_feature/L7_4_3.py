# project

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())

# Print summary statistics for all columns
print(students.describe())

# Calculate mean
math_grade_mean = students.math_grade.mean()
print(f"Mean: {math_grade_mean}")

# Calculate median
math_grade_median = students.math_grade.median()
print(f"Median: {math_grade_median}") # << larger than mean

# Calculate mode
math_grade_mode = students.math_grade.mode()
print(f"Mode: {math_grade_mode}")

# Calculate range
math_grade_range = students.math_grade.max() - students.math_grade.min()
print(f"Range: {math_grade_range}")

# Calculate standard deviation
math_grade_std = students.math_grade.std()
print(f"STD: {math_grade_std}")

# Calculate MAD
math_grade_mad = students.math_grade.mad()
print(f"Mean: {math_grade_mad}")

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
mjob_count = students.Mjob.value_counts()
print(mjob_count)

# Calculate proportion of students with mothers in each job category
mjob_count_rel = students.Mjob.value_counts() / len(students.Mjob)
print(mjob_count_rel)

# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()
