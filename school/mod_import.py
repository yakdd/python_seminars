from data import lessons


def import_unit(dict_u):
    name = input('Введите имя и фамилию студента через пробел: ')
    dict_u[name] = {i: [] for i in lessons}

    return dict_u


def add_discipl(dict_u):
    print('Имеющиеся предметы:', lessons)
    less = input('Добавьте название предмета: ')
    if less not in lessons:
        lessons.append(less)
        for dict_education in dict_u.values():
            dict_education[less] = []
    else:
        print('Такой предмет уже есть в списке!')

    return dict_u
