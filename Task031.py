# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))

prime_mult = []
while n > 0:
    for i in range(2, n + 1):
        if n % i == 0:
            prime_mult.append(i)
            break
    n //= i

if len(prime_mult) == 1:
    prime_mult.insert(0, 1)

print(prime_mult)
