def check_id(id):
    """ Проверка уникальности ID """

    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        for line in file:
            current_id = line.rstrip().split(';')[0]
            if str(id) == current_id:
                print('ID занят. Введите уникальный номер')
                return False
    return True


def input_person():

    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        count_strings = sum([1 for line in file]) - 1
        print('Количество записей в справочнике:', count_strings)

    print('Введите данные:')
    id = int(input('ID: '))
    if check_id(id):
        last_name = input('Фамилия: ')
        first_name = input('Имя: ')
        phone_num = str(input('Телефон: '))
        comment = input('Комментарий: ')

        with open('phonebook.csv', 'a', encoding='utf-8') as phonebook:
            phonebook.write(f'{id};{last_name};{first_name};{phone_num};{comment}\n')

    else:
        input_person()
