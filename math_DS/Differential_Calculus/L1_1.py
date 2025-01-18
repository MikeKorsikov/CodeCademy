# Differential Calculus
# Limits - is the value of a function approaches as we move to some x value.
# derivative - is the slope of a tangent line at a specific point


# Turning our function into an array 
import numpy as np
from math import pow
from math import sin
import matplotlib.pyplot as plt

# our change in x value
dx = 0.01
def f(x):
    return sin(x)
sin_y = [f(x) for x in np.arange(0,20,dx)] 
sin_x = [x for x in np.arange(0,20,dx)]

# Define your derivative here
sin_deriv = np.gradient(sin_y,dx)

plt.plot(sin_x, sin_y)
plt.plot(sin_x, sin_deriv)
plt.show()
