def get_summ(x, y):
    return str(x + y)


def get_diff(x, y):
    return str(x - y)


def get_mult(x, y):
    return str(x * y)


def get_dev(x, y):
    if y != 0:
        return str(x / y)
    else:
        return None


def get_int_dev(x, y):
    if y != 0:
        return str(x // y)
    else:
        return None


def get_rest_dev(x, y):
    if y != 0:
        return str(x % y)
    else:
        return None
