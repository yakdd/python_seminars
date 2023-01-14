import random


k = int(input('Введите степень многочлена: '))

result = ''
for i in range(k, -1, -1):
    koef = random.randint(0, 3)
    if koef == 0:
        continue
    if i == 1:
        if koef > 1:
            result += f"{koef}*x + "
        if koef == 1:
            result += f"x+"
    if i > 1:
        if koef > 1:
            result += f"{koef}*x**{i} + "
        if koef == 1:
            result += f"x**{i} + "
    if i == 0:
        if koef > 1:
            result += f"{koef} + "
        if koef == 1:
            result += f"1 + "

print(result[:-1] + " = 0")
