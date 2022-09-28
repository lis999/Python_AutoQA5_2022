"""
Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
Текст и количество повторений нужно ввести с помощью input()
"""

text = input('Enter your text: ')
repeat = int(input('How many times to repeat? '))

for number in range(repeat):
    print(text)