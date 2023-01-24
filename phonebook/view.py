def select_action():
    print('\nВыберете действие:')
    print('  1 - добавить запись в справочник')
    print('  2 - вывести все записи')
    print('  3 - отсортировать по имени')
    print('  4 - отсортировать по ID')
    print('  5 - вывести имя и фамилию')
    print('  0 - выход')
    action = int(input('> '))
    return action
