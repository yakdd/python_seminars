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
    if dict_u:
        i = 1
        for name, education in dict_u.items():
            print(f'{i}. {name}:')
            for less, score in education.items():
                print(f'\t\t{less}: {score}')
            i += 1
    else:
        print('Журнал не найден.')
        return False


def export_journal(dict_u):
    """ экспорт данных в файл """
    with open('journal.csv', 'w', encoding='utf-8') as file:
        file.write('Ученик;Предмет;Оценки\n')
        for unit, lessons in dict_u.items():
            for less, score_list in lessons.items():
                score_string = ', '.join(list(map(str, score_list)))
                file.write(f'{unit};{less};{score_string}\n')
