def output_info():
    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        max_len_elem = 0
        for line in phonebook:
            for elem in line.rstrip().split(';'):
                if len(elem) > max_len_elem:
                    max_len_elem = len(elem)
        space = max_len_elem + 5

    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        head = phonebook.readline().rstrip().split(';')
        for elem in head:
            print('{0: <{space}}'.format(elem, space=space), end='')
        print()

    print('-' * space * len(head))

    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        for indx, line in enumerate(phonebook):
            if indx < 1:
                continue
            else:
                row = line.rstrip().split(';')
                for elem in row:
                    print('{0: <{space}}'.format(elem, space=space), end='')
                print()

    print('-' * space * len(head))


def output_fio():
    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        for indx, line in enumerate(phonebook):
            if indx < 1:
                continue
            else:
                row = line.rstrip().split(';')
                print(row[2], row[1])
