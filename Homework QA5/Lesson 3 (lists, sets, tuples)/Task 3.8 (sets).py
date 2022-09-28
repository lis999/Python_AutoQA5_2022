"""
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга
"""

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# if set1.issubset(set2) == True:
#     print('Set1 is a subset of Set2')
# else:
#     print('Set1 is not a subset of Set2')
#
# if set2.issubset(set1) == True:
#     print('Set2 is a subset of Set1')
# else:
#     print('Set2 is not a subset of Set1')
#
# for symbol in set1:
#     for symbol1 in set2:
#         if symbol == symbol1:
#             print(symbol, ' - included into both sets')

####################

print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.issuperset(set1))
print(set1.issubset(set2))