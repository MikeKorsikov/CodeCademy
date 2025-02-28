# Percentiles

import numpy as np

d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8])
print(np.percentile(d, 40))

#
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 30)
print(thirtieth_percentile)

seventieth_percentile = np.percentile(patrons, 70)
print(seventieth_percentile)


# interquartile range
movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)
print(first_quarter)

third_quarter = np.percentile(movies_watched, 75)
print(third_quarter)

interquartile_range = third_quarter - first_quarter
print(interquartile_range)