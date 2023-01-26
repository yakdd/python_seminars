def column_width(rows):
    """ Возвращает список ДЛИН самых длиных элементов в столбце """
    columns_list = []
    for k, i_list in enumerate(rows):
        for i in range(len(i_list)):
            if k > 0:
                break
            col_list = []
            for j in range(len(rows)):
                col_list.append(rows[j][i])
            columns_list.append(col_list)

    max_length_element = []
    for column in columns_list:
        width = max(map(len, column))
        max_length_element.append(width)

    return max_length_element


def output_info():
    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        rows_list = [line.rstrip().split(';') for line in phonebook]
        col_width_list = column_width(rows_list)
        empty_space = 5
        hr = sum(col_width_list) + (empty_space * (len(col_width_list) - 1))
        print('-' * hr)

        phonebook.seek(0)
        head = phonebook.readline().rstrip().split(';')
        for indx, elem in enumerate(head):
            space = col_width_list[indx] + empty_space
            print('{0: <{1}}'.format(elem.upper(), space), end='')
        print()
        print('-' * hr)

        phonebook.seek(0)
        for indx, line in enumerate(phonebook):
            if indx < 1:
                continue
            else:
                row = line.rstrip().split(';')
                for indx, elem in enumerate(row):
                    space = col_width_list[indx] + empty_space
                    print('{0: <{1}}'.format(elem, space), end='')
                print()
        print('-' * hr)


def output_fio():
    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        for indx, line in enumerate(phonebook):
            if indx < 1:
                continue
            else:
                row = line.rstrip().split(';')
                print(row[2], row[1])
