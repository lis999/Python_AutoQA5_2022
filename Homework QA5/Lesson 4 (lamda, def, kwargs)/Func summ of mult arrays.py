from functools import *

arr1 = [6, 5, 4, 3, 2]
arr2 = [8, 9, 10, 11, 12, 13]

def sum_arr(arr1, arr2):
    return sum(arr1 + arr2)

def sum_arr2(*args):
    return reduce(lambda x, y: x + y, arr1 + arr2)

print(sum_arr(arr1, arr2))
print(sum_arr2(arr1, arr2))


def average_arr(arr):
    return sum(arr) / len(arr) if len(arr) > 0 else 0
print (average_arr(arr2))