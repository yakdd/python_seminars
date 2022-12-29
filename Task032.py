# 32. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

numbers = [randint(1, 9) for _ in range(9)]
print(numbers)


# Var_#1 ------------------------------
unique_num_1 = []
for i in numbers:
    if numbers.count(i) == 1:
        unique_num_1.append(i)

print(unique_num_1)


# Var_#2 ------------------------------
unique_num_2 = []
for i in range(len(numbers)):
    if numbers[i] not in numbers[0:i] and numbers[i] not in numbers[i+1:]:
        unique_num_2.append(numbers[i])

print(unique_num_2)


# Var_#3 ------------------------------
num_set = set(numbers)
for i in num_set:
    numbers.remove(i)

unique_num_3 = num_set.symmetric_difference(numbers)
print(list(unique_num_3))
