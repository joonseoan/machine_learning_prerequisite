import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20, 10000)
mean = np.mean(incomes)
print("mean1:", mean)
median = np.median(incomes)
print("median1:", median)

incomes = np.append(incomes, [1000])

mean = np.mean(incomes)
print("mean2:", mean)
median = np.median(incomes)
print("median2:", median)

plt.hist(incomes, 50)
plt.show()
