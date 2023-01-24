def new_phonebook():
    try:
        with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
            pass
    except FileNotFoundError:
        with open('phonebook.csv', 'w', encoding='utf-8') as phonebook:
            phonebook.write(f'id;фамилия;имя;номер телефона;комментрий\n')


def rewrite_phonebook(array_of_rows):
    with open('phonebook.csv', 'w', encoding='utf-8') as phonebook:
        phonebook.write(f'id;фамилия;имя;номер телефона;комментрий\n')
        for i, row in enumerate(array_of_rows):
            id = int(row[0])
            last_name = row[1]
            first_name = row[2]
            phone_num = row[3]
            comment = row[4]
            phonebook.write(f'{id};{last_name};{first_name};{phone_num};{comment}\n')
