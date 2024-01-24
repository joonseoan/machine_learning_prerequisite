"""
Python is what is called a dynamically typed language.
It tries to infer the data type of the variables
based on how we initially use them.

We can explicitly cast variables to different types if we need to do so,
but variable won't be recast automatically
"""

"""
  Course tutorial: http://localhost:8888/notebooks/Python101.ipynb
"""

import numpy as np
# 25.0 : mean (center of the distribution)
# 5: standard deviation (Standard deviation (spread or “width”) of the distribution. Must be non-negative.)
# 10: number of random values

# Draw random samples from a normal (Gaussian) distribution.
A = np.random.normal(25.0, 5.0, 10)
print(A)

print("")
print("--------------- list ------------")
x = [1, 2, 3, 4, 5, 6]
print("x: ", x)
print('x[:3]: ', x[:3])
print('x[3:]: ', x[3:])
print('x[-2:]: ', x[-2:]) # 6 - 2

# adding array
x.extend([7, 8])
print('x.extend: ' ,x)
# adding element
x.append(9)
print('x.append(9): ', x)

y = [10, 11, 12]
print('y: ', y)
list_of_lists = [x, y]
print('[x, y]: ', list_of_lists)

list = x + y
print('x + y: ', list)

z = [3, 2, 1]
print("z: ", z)

z.sort()
print("z.sort(): ", z)

# [IMPORTANT]
z.sort(reverse=True)
print("z.sort(reverse='True'): ", z)

z.reverse()
print("z.reverse(): ", z)

print("")
print("---------------------- Tuples -------------------")
# Tuples works like list but the main difference is tuples is immutable. (Can't change)
xx = (1, 2, 3)
print('xx: ', xx)
yy = (1, 2, 3)
print('yy: ', yy)

_list_of_list = [xx, yy]
print("[xx, yy]: ", _list_of_list)

tup = "32,1200000".split(",")
print("'32,1200000'.split(','): ", tup)  # It lis list

# [IMPORTANT]
# Deconstruct list by using tuple
(age, income) = "32,1200000".split(",")
print("age: ", age)
print("income: ", income)


print("")
print("---------------------- Dictionary -------------------")
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print("captains: ", captains)
print("captions[Voyager]: ", captains["Voyager"]) # KeyError
print("captains.get['Enterprise']: ", captains.get("Enterprise")) # No KeyError. Instead it return None


print("")
print("---------------------- Function and Callback -------------------")

def down_to_nearest_number(x, y):
  return x // y

print(down_to_nearest_number(15, 2)) # 7, not 7.5

def square(x):
  return x ** 2

print(square(2))

# [IMPORTANT]
def callback_fun_example(func, x):
  return func(x)

print(callback_fun_example(square, 3)) # 9

# [IMPORTANT]
# lambda functions let us inline simple function (kind of anonymous function?)
# lambda x ==> def func(x)
# : ===> return
# x ** 3 ===> content in the function
# 3 ===> argument value
print("lambda: ", callback_fun_example(lambda x: x ** 3, 3))

print("")
print("---------------------- Boolean -------------------")

print("True or False:", True or False) # True (In any programming language, False can't run)
# [IMPORTANT]
# For operators like &&, ||, or !, 
# we just use the words "and", "or", or "not" instead of special symbols
print("1 is 3:", 1 is 3)

if 1 is 3:
  print("How did that happen")
elif 1 > 3:
  print("Yikes")
else:
  print("All is well with the world")

print("")
print("---------------------- For loop -------------------")

my_list = [0, 1, 2, 5, 8, 3]
for el in my_list:
  if el % 2 is 0:
    print(el)








