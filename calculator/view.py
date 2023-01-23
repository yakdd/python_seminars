def get_value(func):
    return func(input())


def get_type(type):
    if type == '1':
        func = int
    elif type == '0':
        func = complex
    return (func, type)


def get_operation(type):
    sign = input()
    if type == '0' and (sign == '%' or sign == '//'):
        return False
    if type == '1':
        return sign


def answer(data):
    print('=', data)
