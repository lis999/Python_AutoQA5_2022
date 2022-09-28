"""
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
"""

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# total_value = 0
# my_dict_value = my_dictionary.values()
# for number in my_dict_value:
#     if isinstance(number, int):
#         total_value += number
# print('Total: ', total_value)

###### 2nd method
sum_dict = sum(my_dictionary.values())
print(sum_dict)

sum_dict1 = (sum(my_dictionary[item] for item in my_dictionary))
print(sum_dict1)