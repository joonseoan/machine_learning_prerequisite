import numpy as np
import matplotlib.pyplot as plt

# Tomorrow. Let's look at the standard deviation and variance concept more in the internet

# 100.0 : center number
# 20.0 : standard deviation
# 10000: data points
incomes = np.random.normal(100.0, 50.0, 10000)
print(incomes.std())  # standard deviation (square root of variance)
print(incomes.var())  # variance
plt.hist(incomes, 50)
plt.show()
