# This script demonstrates the performance differences between using a list and a generator expression, as well as the benefits of using a generator expression for memory efficiency.

import cProfile
import timeit

# Create a list of squares using a list comprehension
squares_list = [i**2 for i in range(1000000)]

# Create a generator expression of squares
squares_gen = (i**2 for i in range(1000000))

# Define a function that squares each number in a given iterable
def squares(squares):
    for square in squares:
        m = square**2

# Test the performance of the squares function using the list and generator expression
#print(timeit.timeit('squares(squares_list)', globals=globals(), number=100))
#print(timeit.timeit('squares(squares_gen)', globals=globals(), number=100))

# Define a generator function that counts up to a given number
def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

# Create a generator object that counts up to 5
numbers = count_up_to(5)

# Test the generator object by printing the first two numbers
#print(next(numbers))  # Erst jetzt wird die erste Zahl berechnet: 1
#print(next(numbers))  # Jetzt wird die zweite Zahl berechnet: 2

# Define two functions that square a given value a large number of times
# One function uses a global variable, the other takes the value as an argument
# The second function is faster because it avoids the overhead of accessing a global variable
global_var = 5
def func():
    for _ in range(3000000):
        x = global_var**2

def func2(val):
    for _ in range(3000000):
        x = val**2

# Test the performance of the two functions using cProfile
cProfile.run('func()')
cProfile.run('func2(5)')

# Importing modules can be done in two ways: either import the entire module or import specific functions from the module
# Here are two examples of how to import the square root function from the math module
# import math
# value = math.sqrt(50)
#
# from math import sqrt
# value = sqrt(50)