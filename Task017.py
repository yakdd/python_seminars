# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint as rnd


number = int(input('Введите число: '))

n_list = []
for i in range(- number, number + 1):
    n_list.append(i)
print(n_list)


with open('file.txt', 'w+', encoding='utf-8') as file:
    for i in range(3):
        file.write(str(rnd(1, number * 2)) + '\n')

mult = 1
with open('file.txt', 'r', encoding='utf-8') as file:
    count = 0
    for line in file:
        if count < 2:
            print(f' {n_list[int(line)]} *', end='')
        else:
            print(n_list[int(line)], end='')

        mult *= n_list[int(line)]
        count += 1


print(' =', mult)
