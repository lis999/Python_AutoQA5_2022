"""
Напишите программу, которая проверяет здоровье персонажа в игре.
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
"""

while True:
    health = int(input('Enter your health rate: '))
    if health > 0:
        print('True')
    else:
        print('False')