# 38. Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100
# Имеется список имен сотрудников из 10 элементов
# Сопоставьте каждому имени сотрудника его id, и выведите получившийся список.
# Выведете имена сотрудников, получившие нечетное id. Решить с помощью zip,filter,lambda

from random import randint


id = [randint(1, 100) for _ in range(8)]
names = ['ivanov', 'petrov', 'sidorov', 'kuznecov',
         'potapov', 'yakovlev', 'vasilev', 'putin']

names_list = list(zip(id, names))
print(names_list)

lst_odd_id = [elem[1] for elem in names_list if elem[0] % 2 != 0]
print(lst_odd_id)
