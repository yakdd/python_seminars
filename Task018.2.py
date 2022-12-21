import datetime


def random_int(num):
    rand = datetime.datetime.now().microsecond / 10 ** 6
    # print(num, rand, num * rand)
    return int(num * rand)


random_int(5)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print()
print(a)

for i in range(len(a) - 1, 0, -1):
    j = random_int(i)
    # print(a)
    a[i], a[j] = a[j], a[i]

print(a)
