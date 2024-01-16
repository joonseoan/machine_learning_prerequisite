"""
  Course tutorial: 
  http://localhost:8888/notebooks/PandasTutorial.ipynb
  http://localhost:8888/edit/PastHires.csv
"""

"""
It's one of three libraries you'll encounter repeatedly in the field of data science:

Pandas: Introduces "Data Frames" and "Series" that allow you to slice and dice
rows and columns of information.

Numpy: Usually you'll encounter "NumPy arrays", which are multi-dimensional array objects.
It is easy to create a Pandas DataFrame from a NumPy array, 
and Pandas DataFrames can be cast as NumPy arrays.
NumPy arrays are mainly important because of...

Scikit_Learn: The machine learning library we'll use throughout this course is scikit_learn,
or sklearn, and it generally takes NumPy arrays as its input.

So, a typical thing to do is to load, clean, and manipulate your input data using Pandas.
Then convert your Pandas DataFrame into a NumPy array as it's being passed into some Scikit_Learn function.
That conversion can often happen automatically.

Pandas ----> Numpy ----> Scikit_Learn
"""

import numpy as np
import pandas as pd

try:
    df = pd.read_csv("./past_hires.csv")
except FileNotFoundError as message:
    print('message:', message)
else:

    # [head an tail]
    # head() is a handy way to visualize what you've loaded.
    print(" --------------- df.head() ------------------- ")
    print(df.head())  # generates 4 rows

    # You can pass it an integer to see some specific number
    # of rows at the beginning of your DataFrame:
    print(" --------------- df.head(10) ------------------- ")
    print(df.head(10))

    # From the bottom
    print(" --------------- df.tail() ------------------- ")
    print(df.tail())  # generates 4 rows

    # From the bottom up to 4 rows
    print(" --------------- df.tail(4) ------------------- ")
    print(df.tail(4))

    # [shape]: We often talk about the shape of our DataFrame. This is just its dimensions.
    # This particular CSV file has 13 rows and 7 columns for row:
    print(" --------------- df.shape ------------------- ")
    print("df.shape:", df.shape)  # ---> 13, 7

    print(" --------------- df.size ------------------- ")
    print("df.shape:", df.size)  # ---> 91 (13 * 7)

    print(" --------------- len(df) ------------------- ")
    print("len:", len(df))  # ---> row length

    print(" --------------- df.columns ------------------- ")
    print("df.columns", df.columns)  # ---> row length

    print(" --------------- get a specific column ------------------- ")
    print("df['Hired']:", df["Hired"])

    print(" --------------- get a specific column and its rows ------------------- ")
    print("df['Hired'][:5]:", df["Hired"][:5])

    print(" --------------- get a specific column and its single row ------------------- ")
    # [IMPORTANT]
    # We can extract a single row or single column like this
    # that gives us back what is called "series"
    # In other words, "Series" is basically a one dimensional array extracted from the tabular DataFrame.
    print("df['Hired'][5]:", df["Hired"][5])

    print(" --------------- get specific columns ------------------- ")
    print("df[['Hired', 'Years Experience']]:", df[["Years Experience", "Hired"]])

    print(" --------------- get specific columns and its rows ------------------- ")
    print("df[['Years Experience', 'Hired']][:5]:", df[["Years Experience", "Hired"]][:5])

    print(" --------------- Sorting DataFrame by a specific column looks lik this ------------------- ")
    print("df.sort_values(['Years Experience']):", df.sort_values(['Years Experience']))

    print(" --------------- Value Counts ------------------- ")
    degree_counts = df["Level of Education"].value_counts()
    print("degree_counts:", degree_counts)
    # print("df.sort_values(['Years Experience']):", df.sort_values(['Years Experience']))

    print(" --------------- Plot by using Value Count ------------------- ")
    # degree_counts.plot(kind="bar")

    print(" ---------------- Exercise =================================")
    data = df.head(6)
    data = data[["Previous employers", "Hired"]]

    data_count = data["Previous employers"].value_counts()
    data_count.plot(kind="bar")  # Do not worry about the error.





