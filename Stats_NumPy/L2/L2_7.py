import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

rain_mean = np.mean(rainfall)
print(f"Mean: {rain_mean}")

rain_median = np.median(rainfall)
print(f"Median: {rain_median}")

first_quarter = np.percentile(rainfall, 25)
print(f"First Q: {first_quarter}")

third_quarter = np.percentile(rainfall, 75)
print(f"Third Q: {third_quarter}")

interquartile_range = third_quarter - first_quarter
print(f"Range: {interquartile_range}")

rain_std = np.std(rainfall)
print(f"Std: {rain_std}")