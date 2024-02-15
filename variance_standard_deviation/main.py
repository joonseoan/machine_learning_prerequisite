import numpy as np
import matplotlib.pyplot as plt

# 100.0 : center number
# 50.0 : scale for x coord
# 10000: data points
incomes = np.random.normal(100.0, 50.0, 10000)
print("variance:", incomes.var())  # variance
print("standard deviation:", incomes.std())  # standard deviation (square root of variance)
print("mean:", incomes.mean())

plt.hist(incomes, 50)
plt.show()
