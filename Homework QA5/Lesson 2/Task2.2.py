"""
Напишите программу, которая проверяет является ли введенное число четным.
Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
"""

number = int(input('Enter your number: '))
if number % 2 == 0:
    print('Number: ', number, 'is even')
else:
    print('Number: ', number, 'is ODD')