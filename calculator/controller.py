import view
import operation


def button_click():
    print('КАЛЬКУЛЯТОР')
    arithm = input('\
Работа с комплексными числами, введите 0\n\
Работа с целыми числами, введите 1: ')
    convert, type_of_num = view.get_type(arithm)
    value_a = view.get_value(convert)
    oper = view.get_operation(type_of_num)
    value_b = view.get_value(convert)
    data = (oper, value_a, value_b)
    result = operation.get_result(data)
    if result:
        view.answer(result)
    else:
        print('Недопустимая операция')
