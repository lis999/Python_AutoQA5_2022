"""
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
"""

my_list = [1, 2, 3, 4, 5, 3, 2, 1]
sorted_list = set(my_list)
print(*sorted_list)