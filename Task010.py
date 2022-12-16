# 10. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def hypotenuse(point_a, point_b):
    distance = math.sqrt((point_a[0] - point_b[0])
                         ** 2 + (point_a[1] - point_b[1]) ** 2)
    return round(distance, 4)


point_A = list(
    map(int, input('Введите через пробел координаты X и Y первой точки: ').split()))

point_B = list(
    map(int, input('Введите через пробел координаты X и Y второй точки: ').split()))

print(f'Расстояние между точками: {hypotenuse(point_A, point_B)}')
