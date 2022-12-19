# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


number = int(input('Введите число: '))

# VAR#1 -------------------
factorial_list = []
for i in range(1, number + 1):
    factorial_list.append(factorial(i))

print(factorial_list)


# VAR#2 -------------------
multiply_list = [1]
for i in range(2, number + 1):
    multiply_list.append(multiply_list[-1] * (i))

print(multiply_list)
