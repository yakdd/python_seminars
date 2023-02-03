from decimal import Decimal as Dec
import view

operation = ('+', '-', '*', '/', '%')
legal_symbols = (' ', '0', '.', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', 'i', '+', '-', '*', '/', '%')


def check_input(string):
    """ Проверка введенных символов на допустимость """
    for sym in string:
        if sym not in legal_symbols:
            return False
    return True


# rational_parser ==========================================
def negative_parser(math_exp):
    """ Парсинг строки с разностью """
    if not math_exp[0].isdigit() and math_exp[0] != '-':
        view.error(1)
        exit()
    else:
        negative = ''
        if math_exp[0] == '-':
            negative = '-'
            math_exp = math_exp[1:]
        split_ = math_exp.index('-')
        first_num = negative + math_exp[0:split_]
        second_num = math_exp[split_ + 1:]
        return Dec(first_num), Dec(second_num)


def rational_parser(math_exp):
    """ Парсинг строки с действительными числами """
    math_exp = math_exp.replace(' ', '')
    sign = ''
    for i in range(1, len(math_exp) - 1):
        if math_exp[i] in operation:
            if math_exp[i] == '/' and math_exp[i + 1] == '/':
                sign = '//'
                break
            else:
                sign = math_exp[i]
                break

    if sign == '-':
        a, b = negative_parser(math_exp)
        return a, b, sign

    a, b = map(Dec, math_exp.split(sign))
    return a, b, sign


# complex_parser ==========================================
def check_complex_operation(math_exp):
    """ Проверка допустимости мат.операции для комплексных чисел """
    for op in ['//', '%']:
        if op in math_exp:
            return False
    return True


def complex_parser(math_exp):
    """ Парсинг строки с комплексными числами """

    if not check_complex_operation(math_exp):
        result = view.error(2)
        return result

    math_exp = math_exp.replace(' ', '')
    math_exp = math_exp.replace('i', 'j')
    elements = math_exp.split('j')[:-1]

    first_number = complex(elements[0] + 'j')
    second_number = elements[1]
    sign = second_number[0]
    second_number = complex(second_number[1:] + 'j')

    return first_number, second_number, sign


# mixed_parser ==========================================
def mixed_parser(math_exp):
    """ Парсинг смешанной строки """

    if not check_complex_operation(math_exp):
        result = view.error(2)
        return result

    math_exp = math_exp.replace(' ', '')
    math_exp = math_exp.replace('i', 'j')
    elements = math_exp.split('j')

    if elements[1] != '':
        first_number = complex(elements[0] + 'j')
        sign = elements[1][0]
        second_number = complex(elements[1][1:])
        return first_number, second_number, sign

    else:
        negative = ''
        string = elements[0]
        if not elements[0][0].isdigit() and elements[0][0] != '-':
            result = view.error(1)
            return result
        elif elements[0][0] == '-':
            negative = '-'
            string = elements[0][1:]
            if not string[0].isdigit():
                result = view.error(1)
                return result

        first_number = negative
        second_number = sign = ''
        for i, val in enumerate(string):
            if val not in ('+', '-', '*', '/'):
                first_number += val
            else:
                first_number = complex(first_number)
                sign = val
                second_number = complex(string[i + 1:] + 'j')
                break

    return first_number, second_number, sign
