import numpy as np
import matplotlib.pyplot as plt

"""
Uniform Distribution: just means there's a flat constant probability of a value
occurring within a give range. We can use this by using the "np.uniform" function
"""
values = np.random.uniform(-10.0, 10.0, 100000)

plt.hist(values, 50)
plt.show()