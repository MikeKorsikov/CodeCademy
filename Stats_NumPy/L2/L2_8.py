# project

import numpy as np

print("Exercise 2:")
calorie_stats = np.genfromtxt('Codecademy\Stats_NumPy\L2\cereal.csv', delimiter = ",")
print(calorie_stats)

print("\nExercise 3:")
average_calories =  np.mean(calorie_stats)
print(f"Average: {average_calories}")

print("\nExercise 4:")
calorie_stats_sorted = np.sort(calorie_stats)
print(f"Sorted: {calorie_stats_sorted}")

print("\nExercise 5:")
median_calories = np.median(calorie_stats)
print(f"Median: {median_calories}")

print("\nExercise 6:") # << not sure
nth_percentile = None
for i in range(101):
    percentile_value = np.percentile(calorie_stats, i)
    if percentile_value > 60:
        nth_percentile = i
        break
print(nth_percentile)

print("\nExercise 7:")
more_calories = np.mean(calorie_stats > 60)
print("Percentage of cereals with more than 60 calories:", more_calories, "%")

print("\nExercise 8:")
calorie_std = np.std(calorie_stats)
print(f"Std: {calorie_std }")
