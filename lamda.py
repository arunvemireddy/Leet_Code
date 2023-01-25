# lamda can take any number of arguments but can have only one expression

def test(b):
    return lambda a:a*b

x = test(5)
print(x(6))


y = lambda a, b ,c : (a * b)/c
print(y(1,2,3))