# модуль для расчетов операций
def sum(left_value, right_value):
    return left_value + right_value

def sub(left_value, right_value):
    return left_value - right_value

def mult(left_value, right_value):
    return left_value * right_value

def div(left_value, right_value):
    return left_value / right_value

def calc_block(left_value, oper, right_value):
    if oper == '+':
        res = sum(left_value, right_value)
    if oper == '-':
        res = sub(left_value, right_value)
    if oper == '*':
        res = mult(left_value, right_value)
    if oper =='/' and right_value != 0:
        res = div(left_value, right_value)
    if oper =='/' and right_value == 0:
        res = 'Ошибка деления на 0!'
    return res




