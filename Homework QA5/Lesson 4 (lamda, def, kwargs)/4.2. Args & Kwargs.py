"""
Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно в формате
аргумент: значение. Например:
name: John
last_name: Smith
age: 35
position: web developer
"""
def print_args(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {str(value)}')

print_args(name = 'John', last_name = 'Smith', age = 35, position = 'web developer')
print()
print_args(make = 'Honda', model = 'Insight', year = 2022, color = 'Blue')