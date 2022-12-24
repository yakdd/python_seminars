
# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def nok_nod(x, y):
    mult = x * y
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    nod = x

    # Var_2 -------------------
    # first = max(x, y)
    # second = min(x, y)
    # while True:
    #     rest = first % second
    #     if rest == 0:
    #         break
    #     first = second
    #     second = rest
    # nod = second
    # -------------------------

    nok = int(mult / nod)
    return (nod, nok)


a = int(input('A: '))
b = int(input('B: '))


# Var_#1 ---------------------------
for i in range(max(a, b), a * b + 1, max(a, b)):
    if i % a == 0 and i % b == 0:
        print('nok =', i)
        break

# Var_#2 ---------------------------
result = nok_nod(a, b)
print('Наибольший общий делитель:', result[0])
print('Наименьшее общее кратное:', result[1])
