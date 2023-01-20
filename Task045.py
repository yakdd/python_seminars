# 45. Найти сумму чисел списка стоящих на нечетной позиции
from random import randint

num = [randint(1, 10) for _ in range(10)]
print(num)

odd_num = [val for i, val in enumerate(num) if i % 2]
print(sum(odd_num))
