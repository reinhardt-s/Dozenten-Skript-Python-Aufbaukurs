# Mit Liste
import cProfile
import timeit

squares_list = [i**2 for i in range(1000000)]
squares_gen = (i**2 for i in range(1000000))

def squares(squares):
    for square in squares:
        m = square**2

#print(timeit.timeit('squares(squares_list)', globals=globals(), number=100))
#print(timeit.timeit('squares(squares_gen)', globals=globals(), number=100))

def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1


numbers = count_up_to(5)


#print(next(numbers))  # Erst jetzt wird die erste Zahl berechnet: 1
#print(next(numbers))  # Jetzt wird die zweite Zahl berechnet: 2



# Langsamer
global_var = 5
def func():
    for _ in range(3000000):
        x = global_var**2


# Schneller
def func2(val):
    for _ in range(3000000):
        x = val**2


cProfile.run('func()')
cProfile.run('func2(5)')


# import math
# value = math.sqrt(50)
#
#
# from math import sqrt
# value = sqrt(50)