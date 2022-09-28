"""
3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""

family_1 = input('Enter your family member name: ')
family_2 = input('Enter your family member name: ')
# print(family_1)
# print(family_2)

def count_members(family):
    count = 0
    for member in family:
        count += 1
    return count

family1_count = count_members(family_1)
family2_count = count_members(family_2)

if family1_count > family2_count:
    print(family_1, ' is bigger than', family_2)
elif family1_count < family2_count:
    print(family_2, ' is bigger than', family_1)
else:
    print(family_1, ' and ', family_2, ' are equal')