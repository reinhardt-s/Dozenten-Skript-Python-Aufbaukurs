# Importing necessary libraries
import numpy as np
import pandas as pd
import timeit

# Creating a list of numbers
numbers = list(range(1, 10000001))

# Converting the list into a pandas series object
numbers_series = pd.Series(numbers)

# Function to calculate mean using pure Python
def mean_native(numbers):
    sum(numbers) / len(numbers)

# Function to calculate mean using pandas
def mean_panda(numbers):
    numbers_series.mean()

# Creating two numpy arrays and two lists
a = np.array([1, 2, 3, 4] * 1000000)
b = np.array([5, 6, 7, 8] * 1000000)
c = [1, 2, 3, 4] * 1000000
d = [5, 6, 7, 8] * 1000000

# Function to add two arrays using pure Python
def add_arrays_native(a, b):
    return [a[i] + b[i] for i in range(len(a))]

# Function to add two arrays using numpy
def add_arrays(a, b):
    return a + b

# Creating a pandas DataFrame of people
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [17, 22, 15, 25, 18]
})

# Creating a list of dictionaries of people
personen = [{'Name': 'Alice', 'Age': 17}, {'Name': 'Bob', 'Age': 22},
            {'Name': 'Charlie', 'Age': 15}, {'Name': 'David', 'Age': 25}, {'Name': 'Eve', 'Age': 18}]

# Function to filter people above 18 years of age using pandas
def filter_18plus():
    return df[df['Age'] > 18]

# Function to filter people above 18 years of age using pure Python
def filter_18plus_native():
    return [person for person in personen if person['Age'] > 18]
