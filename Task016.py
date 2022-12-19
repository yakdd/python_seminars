# 16. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def sequence(n):
    return round((1 + 1 / n) ** n, 2)


number = int(input('Введите число: '))

seq_dict = {}
for i in range(1, number + 1):
    seq_dict[i] = sequence(i)

print(f'Для n = {number} {seq_dict}')
print(f'Сумма {sum(list(seq_dict.values()))}')
