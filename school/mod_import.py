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


def import_journal():
    """ Импорт данных из файла """
    try:
        with open('journal.csv', 'r', encoding='utf-8') as file:
            file.readline()
            name_list = list(set([line.split(';')[0] for line in file]))

            file.seek(0)
            file.readline()
            units = []
            for line in file:
                row = line.rstrip().split(';')
                units.append(row)

        dict_u = {}
        for name in name_list:
            education_dict = {}
            for row in units:
                if row[0] == name:
                    education_dict[row[1]] = row[2].split(', ')
            dict_u[name] = education_dict

        return dict_u

    except FileNotFoundError:
        print('Журнал не найден.')

        return False

