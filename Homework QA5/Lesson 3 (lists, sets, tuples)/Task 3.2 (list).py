"""
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# finalNumber = 0
# for item in list_1:
#     if isinstance(item, str):
#         if 'a' in str(item):
#             print(item)
#     elif isinstance(item, int):
#         finalNumber += item
# print(finalNumber)

#############
print('Original list - ', list_1)
print('Sum of all numers: ', sum([x for x in list_1 if type(x) == int]))
print('All words with a: ', [y for y in list_1 if type(y) == str and 'a' in y])