# Данная программа должна вывести n рядов, заполненных знаком ‘*’ определенным образом.
# А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее.
# А в последнем ряду таким образом будет одна «звездочка».
# Причем убывать эти «звездочки» должны справа налево. Число n вводится пользователем.
# Введите количество рядов: 5
# *****
# ****
# ***
# **
# *

n = int(input('Введите число: '))

for i in range(n, 0, -1):
    print('*' * i)
