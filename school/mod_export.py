def unit_list(dict_u):
    unit_l = list(dict_u.keys())
    for fio in unit_l:
        print(fio)


def rating_list(dict_u):
    unit = input('Выберете ученика из списка: ')
    for less, score_list in dict_u[unit].items():
        print(f'{less}:', end='\t')
        print(', '.join(list(map(str, score_list))))


def output(dict_u):
    i = 1
    for key, val in dict_u.items():
        print(f'{i}. {key}: {val}')
        i += 1
