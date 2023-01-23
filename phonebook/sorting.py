import initialization


def sorting_phonebook(indx):
    rows = []
    with open('phonebook.csv', 'r', encoding='utf-8') as phonebook:
        for line in phonebook:
            elements = line.rstrip().split(';')
            rows.append(list(map(str, elements)))

    rows = rows[1:]
    sort_rows = sorted(rows, key=lambda x:
                       int(x[indx]) if indx == 0 else x[indx])

    initialization.rewrite_phonebook(sort_rows)
