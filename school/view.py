def select_action():
    print('Выберете действие:')
    print('  1 - добавить студента')
    print('  2 - добавить предмет')
    print('  3 - отсортировать по имени')
    print('  4 - отсортировать по ID')
    print('  5 - вывести имя и фамилию')
    action = int(input(': '))
    return action
