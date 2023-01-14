import random


k = int(input('Введите натуральную степень k: '))

coef_list = [random.randint(0, 5) for _ in range(k + 1)]
for i, val in enumerate(coef_list):
    print(f'[i:{i}|k:{val}]', end='  ')
print()

polynomial = ''

for i in range(k, -1, -1):
    if coef_list[i] == 0:
        continue
    if coef_list[i] == 1:
        polynomial += ('x' if i != 0 else '') \
            + ('**' + str(i) if i > 1 else '') \
            + (' + ' if i != 0 else '')
    else:
        polynomial += (str(coef_list[i]) if coef_list[i] > 1 else '') \
            + ('*' if coef_list[i] > 1 and i != 0 else '') \
            + ('x' if i != 0 else '') \
            + (('**' + str(i)) if i > 1 else '') \
            + (' + ' if i != 0 else '')
polynomial += ' = 0'

print(polynomial)

with open('polynomial.txt', 'w', encoding='utf-8') as file:
    file.write(polynomial)


# path = 'polynomial.txt'
# with open(path, 'w') as data:
#     for i in range(k, -1, -1):
#         if coef_list[i] == 0:
#             continue
#         data.write(str(coef_list[i]) + ('*x' if i != 0 else ''))
#         data.write(('**'+str(i)) if i > 1 else '')
#         data.write(' + ' if i != 0 else '')
#     data.write(' = 0')
