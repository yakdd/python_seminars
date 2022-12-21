# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# n вводит пользователь вывести рандомное число в диапазоне от 0 до n
import datetime

# def rand(n):
#     1:
#     rnd = datetime.datetime.now().microsecond / 10**6
#     return int(rnd * n)
#     2:
#     rnd = datetime.datetime.now().microsecond % n
#     return rnd + 1


def rand_1(n):
    rnd = datetime.datetime.now().microsecond
    rnd = int(str(rnd)[0])
    return int(1 / rnd * n)


def rand_2(n):
    rnd = datetime.datetime.now().microsecond % n
    return rnd + 1


def rand_3(n):
    rnd = datetime.datetime.now().microsecond / 10**6
    return int(rnd * (n + 1))


num = int(input('\nВведите число: '))

# print('1:', rand_1(num))
# print('2:', rand_2(num))
print('3:', rand_3(num))
