from data import lessons


def add_score(dict_u):
    unit = input('Выберете ученика: ')
    if unit in dict_u.keys():
        discipl_to_score = input('Выберете предмет: ')
        if discipl_to_score in lessons:
            rating = int(input('Поставьте оценку (от 2 до 5): '))
            dict_u[unit][discipl_to_score].append(rating)
        else:
            print('Такого предмета нет в списке!')
    else:
        print('Такого ученика нет в списке!')

    return dict_u


def average_rating(dict_u):
    unit = input('Выберете ученика: ')
    if unit in dict_u.keys():
        for less, score_lisr in dict_u[unit].items():
            if len(score_lisr) == 0:
                continue
            avg = round(sum(score_lisr) / len(score_lisr), 1)
            print(f'{less}: {avg}')
    else:
        print('Такого ученика нет в списке!')
