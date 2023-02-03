def user_input():
    print('\nВведите строку с математическим выражением для вычисления результата.', end=' ')
    print('(Например: 12 * 4)')
    print('Операции возможны как с действительными, так и с комплексными (a + bi) числами!')
    string = input('>>> ')
    return string


def result_output(expression, result):
    """ expression - кортеж: (число_1, число_2, операция) """
    if not result:
        error(4)
    else:
        if 'j' in result:
            complex_exp = [expression[0], expression[1], result]
            sign = expression[2]
            expression = []
            for elem in complex_exp:
                elem = str(elem)
                elem = elem[1:-1].replace('j', 'i')
                expression.append(elem)
            print(f'{expression[0]} {sign} {expression[1]} = {expression[2]}')
        else:
            print(
                f'{expression[0]} {expression[2]} {expression[1]} = {result}')


def error(code):
    banner = ''
    if code == 1:
        banner = 'Ошибка ввода!'
    elif code == 2:
        banner = 'Недопустимые символы!'
    elif code == 3:
        banner = 'Недопустимая операция!'
    elif code == 4:
        banner = 'На ноль делить нельзя!'

    print(banner)
