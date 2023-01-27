import random
from data import disciplins
from data import first_names_list as fn
from data import last_names_list as ln


def demo_dict(dict_units):
    num = int(input('На сколько учеников создать демо-версию? '))

    for _ in range(num):
        fio = random.choice(fn) + ' ' + random.choice(ln)
        dict_units[fio] = {i: [random.randint(2, 5) for _ in range(random.randint(0, 5))] for i in disciplins}

    return dict_units
