import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print('(((((((                Mode                ))))))')
ages = np.random.randint(low=18, high=90, size=100)
print(ages)
print(stats.mode(ages))

print("")
print('(((((((         Mean and Median             ))))))')
# np.random.normal: create a random distribution. It creates a bell curve distribution
# of data around a certain point. In this case $27,000 with a standard deviation 15,000
# and we want 10,000 data points in this data set.
incomes = np.random.normal(27000, 15000, 10000)

# Then, compute the mean (average) - it should be close to 27,000:
# because there is a random component to this, the result may be slight different
# whenever run this average
print(np.mean(incomes))

# because the center is also $27,000
# the median also may be around $27,000
print(np.median(incomes))

# Adding a big number!!!! to see how the normal distribution histogram is changed
# Now we will add Jeff Bezos into the mix. Darn income inequality
incomes = np.append(incomes, [1000000000])

print("")
print("--------------- After Jeff Bezos incomes ----------------")
print(np.mean(incomes))  # Definitely it has a big change
print(np.median(incomes))  # Slightly different but almost same


# It is required only when we use jupyter notebook
# If we miss this line, in notebook, it will not display the graphs
# %matplotlib inline

# `hist`: create histogram
# 50: we want to this split up `incomes` into 50 different buckets
# So we are going to quantize our data set into 50 discrete buckets of data
# As this number increases, the graph is more detail
plt.hist(incomes, 10)
plt.show()

