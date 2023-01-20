# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
from random import randint, choice

num = [randint(1, 10) for _ in range(choice([5, 6]))]
print(num)

mult_lst = [num[i] * num[-(i + 1)] for i in range(len(num) // 2 + len(num) % 2)]
print(mult_lst)
