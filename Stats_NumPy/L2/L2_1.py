# mean

import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])



store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)

print(store_one_avg)
print(store_two_avg)
print(store_three_avg)

best_seller = store_two