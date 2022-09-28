"""
Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""

import math
def square(square_side: float) -> tuple:
    square_per = (square_side + square_side) * 2
    square_area = square_side * square_side
    square_diag = math.sqrt((square_side ** 2 + square_side ** 2))
    return (square_per, round(square_area, 2), round(square_diag, 2))
print(square(2.3))

# from my_calc import *
# side1 = float(input('Enter square side: '))
# squareS = calc_square_area(side1)
# perimetr = calc_perim_of_square(side1)
# diagonal = calc_diagonal_of_square(side1)
# print((squareS, perimetr, diagonal), sep = ', ')