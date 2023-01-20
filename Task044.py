# 44. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math

point_a = list(
    map(int, input('Координаты первой точки (через пробел): ').split()))
point_b = list(
    map(int, input('Координаты второй точки (через пробел): ').split()))

hypotenuse = math.sqrt(
    sum(map(lambda x: (x[1] - x[0]) ** 2, zip(point_a, point_b))))
print(f'Расстояние между точками: {round(hypotenuse, 3)}')
