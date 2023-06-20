import numpy as np
import pandas as pd
import timeit

# Große Liste von Zahlen
numbers = list(range(1, 10000001))
numbers_series = pd.Series(numbers)
# Berechnung des Durchschnitts mit reinem Python
def mean_native(numbers):
    sum(numbers) / len(numbers)

# Umwandlung der Liste in ein Pandas Series-Objekt


# Berechnung des Durchschnitts mit Pandas
def mean_panda(numbers):
    numbers_series.mean()

# print(timeit.timeit('mean_native(numbers)', globals=globals(), number=200))
# print(timeit.timeit('mean_panda(numbers_series)', globals=globals(), number=200))



a = np.array([1, 2, 3, 4] * 1000000)
b = np.array([5, 6, 7, 8] * 1000000)

c = [1, 2, 3, 4] * 1000000
d = [5, 6, 7, 8] * 1000000

def add_arrays_native(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def add_arrays(a, b):
    return a + b

# print(timeit.timeit('add_arrays_native(c, d)', globals=globals(), number=50))
# print(timeit.timeit('add_arrays(a, b)', globals=globals(), number=50))


# Angenommen, wir haben eine DataFrame von Personen
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Alter': [17, 22, 15, 25, 18]
})
personen = [{'Name': 'Alice', 'Alter': 17}, {'Name': 'Bob', 'Alter': 22},
            {'Name': 'Charlie', 'Alter': 15}, {'Name': 'David', 'Alter': 25}, {'Name': 'Eve', 'Alter': 18}]

def filter_18plus():
    return df[df['Alter'] > 18]



def filter_18plus_native():
    return [person for person in personen if person['Alter'] > 18]

# print(timeit.timeit('filter_18plus()', globals=globals(), number=100))
# print(timeit.timeit('filter_18plus_native()', globals=globals(), number=100))