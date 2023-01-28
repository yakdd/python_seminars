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
        for less, score_list in dict_u[unit].items():
            if len(score_list) == 0 or score_list[0] == '':
                continue
            avg = round(sum(map(int, score_list)) / len(score_list), 1)
            print(f'{less}: {avg}')
    else:
        print('Такого ученика нет в списке!')


def medalists_show(dict_u):
    medalists = {}
    for unit, education in dict_u.items():
        marks = []
        for lesson, scores in education.items():
            score = list(map(lambda x: int(x) if x else 0, scores))
            marks.extend(score)
        if all(map(lambda x: True if x > 3 else False, marks)):
            medalists[unit] = education

    return medalists


def average_mark(dict_u):
    task = input('Введите предмет: ')
    lesson_marks = []
    for i, lessons in dict_u.items():
        for less in lessons.keys():
            if less == task:
                lesson_marks.extend(lessons[less])

    empty = lesson_marks.count('')
    for _ in range(empty):
        lesson_marks.remove('')
    avg_mark = list(map(int, lesson_marks))
    avg_mark = sum(avg_mark) / len(avg_mark)

    print(f'Средний балл по {task} = {round(avg_mark, 1)}')
