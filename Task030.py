# 30. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
from random import randint


d = 10 ** -randint(1, 10)
print('Точность вычисления:', d)

if '.' in str(d):
    precs = len((str(d)).split('.')[1])
elif '-' in str(d):
    precs = int((str(d)).split('-')[1])

print(
    f'Число \u03C0 с точностью до {precs} знака после запятой: {round(pi, precs)}')
