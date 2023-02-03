def result_output(expression, result):
    """ expression - кортеж: (число_1, число_2, операция) """
    if not result:
        result = error(2)
    else:
        if 'j' in result:
            complex_exp = [expression[0], expression[1], result]
            sign = expression[2]
            expression = []
            for elem in complex_exp:
                elem = str(elem)
                elem = elem[1:-1].replace('j', 'i')
                expression.append(elem)
            result = f'{expression[0]} {sign} {expression[1]} = {expression[2]}'
        else:
            result = f'{expression[0]} {expression[2]} {expression[1]} = {result}'
    
    return result


def error(code):
    banner = ''
    if code == 1:
        banner = 'Недопустимые символы!'
    elif code == 2:
        banner = 'Недопустимая операция!'

    return banner
