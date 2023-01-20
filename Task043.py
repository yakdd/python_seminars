# 43. Напишите программу, которая сортирует отдельно элементы массива с чётными и нечётными значениями.
# Все элементы с нечётными значениями нужно отсортировать по возрастанию,
# а элементы с чётными значениями – по убыванию. При этом элементы каждой из групп(как чётные, так и нечётные)
# должны занимать то же множество позиций в массиве, что и до сортировки.
# Входные данные
# 6
# 3 1 2 5 4 6
# Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива.
# Гарантируется, что 0 < N ≤ 100000 .
# Выходные данные
# 1 3 6 5 4 2
# (1, 1), (0, 3), (3, 5), (5, 6), (4, 4), (2, 2)
# (1, 1), (0, 3), (5, 6), (3, 5),  (4, 4), (2, 2)
# Программа должна вывести все элементы отсортированного массива в одну строку, разделив их пробелами.
# lambda, filter
num = [3, 1, 2, 5, 4, 6]
print(num)


# Var_1 =====================================
indexes = [i for i, v in enumerate(
    num) if v % 2 == 1] + [i for i, v in enumerate(num) if v % 2 == 0]

odd_elem = [v for v in num if v % 2 == 1]
even_elem = [v for v in num if v % 2 == 0]
elements = sorted(odd_elem) + sorted(even_elem, reverse=True)

index_elem = list(zip(indexes, elements))

index_elem_sort = sorted(index_elem, key=lambda x: x[0])
result = [i[1] for i in index_elem_sort]
print(result)


# Var_2 =====================================
numbers = [3, 1, 2, 5, 4, 6]

even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 == 1]
even.sort(reverse=True)
odd.sort()

for indx, value in enumerate(numbers):
    if value % 2 == 0:
        numbers[indx] = even.pop(0)
    else:
        numbers[indx] = odd.pop(0)
print(numbers)
