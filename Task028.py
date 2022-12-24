# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
import math


a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

D = b ** 2 - 4 * a * c
print('D =', D)

if a != 0:
    if D > 0:
        x_1 = (-b + math.sqrt(D)) / (2 * a)
        x_2 = (-b - math.sqrt(D)) / (2 * a)
        print('x1 =', round(x_1, 2))
        print('x2 =', round(x_2, 2))
    elif D == 0:
        x = -b / (2 * a)
        print('x =', round(x, 2))
    else:
        print('Нет решений')

else:
    x = -c / b
    print(x)
