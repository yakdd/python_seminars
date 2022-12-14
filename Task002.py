# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# var_1 ================================
max_num = int(input(f'Введите 1 число: '))

for i in range(4):
    num = int(input(f'Введите {i + 2} число: '))
    if num > max_num:
        max_num = num

print(max_num)


# num_lst = []
# for i in range(5):
#     num = int(input(f'Введите {i + 1} число: '))
#     num_lst.append(num)

# print(max(num_lst))

# max_num = num_lst[0]
# for num in num_lst:
#     if num > max_num:
#         max_num = num


# var_2 ================================
a = input('Введите числа через пробел: ')
print(max(list(map(int, a.split(" ")))))
