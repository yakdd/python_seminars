# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Для чисел:
#   Входные данные:
#   111112222334445
#   Выходные данные:
#   5142233415
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Для букв:
#   Входные данные:
#   AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
#   Выходные данные:
#   6A1F2D7C1A17E
#   6A1F2D7C1A17E
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def rle_coder(string):
    ''' функция сжатия RLE '''
    lst = []
    temp = string[0]
    pos = 0

    for i, val in enumerate(string):
        if val == temp:
            continue
        else:
            lst.append(str(i - pos))
            lst.append(string[i - 1])
            temp = string[i]
            pos = i
    lst.append(str(i - pos + 1))
    lst.append(string[i])
    rle_str = ''.join(lst)
    return rle_str


def rle_decoder(string):
    ini_str = ''
    for i in range(0, len(string), 2):
        ini_str += string[i + 1] * int(string[i])

    return ini_str


ini_str_1 = '111112222334445'
ini_str_2 = 'AAAAAAFDDCCCCCCCAEEEEEEEEE'

print('ini str:', ini_str_1)
result_1_coder = rle_coder(ini_str_1)
print('rle cod:', result_1_coder)
result_1_decoder = rle_decoder(result_1_coder)
print('rle dec:', result_1_decoder)

print()

print('ini str:', ini_str_2)
result_2_coder = rle_coder(ini_str_2)
print('rle cod:', result_2_coder)
result_2_decoder = rle_decoder(result_2_coder)
print('rle dec:', result_2_decoder)
