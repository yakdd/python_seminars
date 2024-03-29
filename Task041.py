# 41. Напишите программу, которая сортирует элементы массива по возрастанию последней цифры десятичной записи чисел.
# Входные данные
# 6
# 219 234 890 81 73 96
# Первая строка содержит размер массива N .
# Во второй строке через пробел задаются N чисел – элементы массива.
# Гарантируется, что 0 < N ≤ 1000 .
# Выходные данные
# 890 81 73 234 96 219
# Программа должна вывести в одной строке элементы массива, отсортированного в порядке возрастания последней цифры
# в десятичной записи чисел, разделив их пробелами.
# Числа, у которых последняя цифра одинаковая, должны быть выведены в том же порядке,
# в котором они стояли в исходной последовательности.

string = '219 234 890 81 73 96'
numbers = list(map(int, string.split()))
num = sorted(numbers, key=lambda x: x % 10)
print(num)
