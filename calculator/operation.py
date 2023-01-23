def get_result(data):
    oper, a, b = data
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        return a / b
    elif oper == '//':
        return a // b
    elif oper == '%':
        return a % b
