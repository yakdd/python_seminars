# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# num = input('Введите дробь: ')

# # var_1 ================================
# if ',' in num:
#     a = num.split(',')
#     print(a[1][0])
# elif '.' in num:
#     a = num.split('.')
#     print(a[1][0])
# else:
#     print('no')


# # var_2 ================================
# num = input()
# list_num = num.split(".")
# if len(list_num) > 1:
#     print(list_num)
#     print(list_num[1][0])


# var_3 ================================
num = float(input('Введите дробь: '))

if int(num) == num:
    print('no')
else:
    print(int(num * 10 % 10))
