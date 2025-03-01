import numpy as np
from matplotlib import pyplot as plt

#
emails = np.random.binomial(500, 0.05, size=10000)

#
plt.hist(emails, range=(0, 100), bins=100)
plt.show()

# probability that no one opens the email
no_emails = np.mean(emails == 0)
print(no_emails)

# probability that 8% or more of people will open the email
b_test_emails = np.mean(emails >= (0.08*500))
print(b_test_emails)