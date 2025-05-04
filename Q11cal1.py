def add1(x, y):
    return x + y

def sub1(x, y):
    return x - y

def mul1(x, y):
    return x * y

def div1(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def mod1(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot find modulo with zero"

def pow1(x, y):
    return x ** y
