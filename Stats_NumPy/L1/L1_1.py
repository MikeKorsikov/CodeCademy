# [row,column] or [axis=1, axis=0]
# a[2,1] where returned number from the 2nd row and 1st column
# selection on axis = 1 (rows)
import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[-2]
manual_adwoa_test_1 = test_1[1:3]
print(manual_adwoa_test_1)

# selecting on axis = 0 (columns)
tanya_test_3 = student_scores[2,0]
print(tanya_test_3)

cody_test_scores = student_scores[:,-1]
print(cody_test_scores)
