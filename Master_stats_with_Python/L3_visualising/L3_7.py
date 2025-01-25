# boxplot

import numpy as np
from data import dataset

# Step 1, Define dataset_median here:
dataset_median = round(np.median(dataset),2)

#Ignore the code below here
try:
  print("The median of the dataset is " + str(dataset_median) + ".")
except NameError:
  print("You haven't defined dataset_median")


# Step 2, Define quartile_one and quartile_three here:
quartile_one = round(np.quantile(dataset, 0.25),2)
quartile_three = round(np.quantile(dataset, 0.75),2)

#Ignore the code below here
try:
  print("The first quartile of the dataset is " + str(quartile_one) + ".")
except NameError:
  print("You haven't defined quartile_one.")
try:
  print("The third quartile of the dataset is " + str(quartile_three) + ".")
except NameError:
  print("You haven't defined quartile_three.")

# Step 3, whiskers - 
# 1.5 times the interquartile range from the first and third quartile
# Define your variables here:
iqr = quartile_three - quartile_one
distance = round(iqr * 1.5,2)
left_whisker = round(quartile_one - distance,2)
right_whisker = round(quartile_three + distance,2)

#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
  
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
  
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
  
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")


# Step 4, outliers
