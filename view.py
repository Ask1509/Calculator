#
def get_type():
    oper_type = input('Enter operation type (real - 1, complex - 0): ')
    for i in oper_type:
        if i in "10":
            continue
        else: oper_type = oper_type.replace(i,'')
    return '1' if oper_type == "" else oper_type

def get_oper():
    oper = input('Enter operational sign(+,-,*,/): ')
    for i in oper:
        if i in "+-*/":
            continue
        else: oper = oper.replace(i,'')
    return oper

def get_value():
    a = input('Enter value: ')
    for i in a:
        if i in "0123456789.-":
            continue
        else: a = a.replace(i,'')
    return eval(a)

def get_complex_value():
    r = input('Enter real part of value = ')
    for i in r:
        if i in "0123456789.-":
            continue
        else: r = r.replace(i,'')
    
    j = input('Enter imaginary part of value = ')
    for i in j:
        if i in "0123456789.-":
            continue
        else: j = j.replace(i,'')
    return complex(eval(r),eval(j))
   