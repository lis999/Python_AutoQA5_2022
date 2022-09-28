"""
Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
Примените эти функции в качестве методов в другом файле.
"""
import math
def calc_square_area(side):
    return round(side ** 2, 2)

def calc_perim_of_square(side):
    return round(side * 4, 2)

def calc_diagonal_of_square(side):
    return round(math.sqrt(side ** 2 + side ** 2), 2)

def calc_half_side(side):
    return round(side / 2, 2)

def division(x, y):
    # assert y != 0, на ноль делить нельзя
    try:
        return round(x/y, 2)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

# print(calc_square_area(5.2))
# print(calc_perim_of_square(5.3))
# print(calc_diagonal_of_square(5.6))
# print(calc_half_side(5.5))