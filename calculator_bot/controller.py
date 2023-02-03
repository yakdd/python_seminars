import view
import my_parser
import math_functions


def calculator():
    string = view.user_input()

    if my_parser.check_input(string):

        math_expression = result = ''
        parse = string.count('i')
        try:
            if parse == 0:
                math_expression = my_parser.rational_parser(string)
            elif parse == 2:
                math_expression = my_parser.complex_parser(string)
            elif parse == 1:
                math_expression = my_parser.mixed_parser(string)
            else:
                view.error(1)

            if math_expression:
                if math_expression[2] == '+':
                    result = math_functions.get_summ(
                        math_expression[0], math_expression[1])
                if math_expression[2] == '-':
                    result = math_functions.get_diff(
                        math_expression[0], math_expression[1])
                if math_expression[2] == '*':
                    result = math_functions.get_mult(
                        math_expression[0], math_expression[1])
                if math_expression[2] == '/':
                    result = math_functions.get_dev(
                        math_expression[0], math_expression[1])
                if math_expression[2] == '//':
                    result = math_functions.get_int_dev(
                        math_expression[0], math_expression[1])
                if math_expression[2] == '%':
                    result = math_functions.get_rest_dev(
                        math_expression[0], math_expression[1])

                view.result_output(math_expression, result)

        except:
            view.error(1)
    else:
        view.error(2)
