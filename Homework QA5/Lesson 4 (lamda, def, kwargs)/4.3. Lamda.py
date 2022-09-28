"""
Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа

Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
"""

from functools import reduce

my_list = [20, -3, 15, 2, -1, -21]
print(f'Initial list: {my_list}')

my_list_posit = list(filter(lambda x: x > 0, my_list))
print(f'Positive values: {my_list_posit}')

my_list_mult = reduce(lambda x, y: x * y, my_list)
print(f'Multiplication result: {my_list_mult}')

#is used to apply a specific function passed in its argument to all of the iterable items mentioned in the sequence passed along