# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = int(input('Введите число: '))

fibonacci = [0, 1]
for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])


fibonacci_neg = [0, 1]
for i in range(2, n + 1):
    fibonacci_neg.append(fibonacci_neg[i - 2] - fibonacci_neg[i - 1])

new_list = list(reversed(fibonacci_neg))
new_list.extend(fibonacci)
new_list.remove(0)
print('VAR_#1:', new_list)
