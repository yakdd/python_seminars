def select_action():
    print('Выберете действие:')
    print('  1 - добавить студента')
    print('  2 - добавить предмет')
    print('  3 - добавить оценки ученику по предмету')
    print('  4 - показать список учеников')
    print('  5 - показать лист оценок ученика')
    print('  6 - показать среднюю оценку ученика по предметам')
    print('  7 - показать средний балл по школе по конкретному предмету')
    print('  8 - показать медалистов')
    print('  9 - показать все данные')
    print('  77 - экспортировать данные в журнал')
    print('  88 - импортировать данные из журнала')
    print('  99 - создать демо-версию журнала')
    print('  0 - выход')
    action = int(input('> '))
    return action