# x = lambda a:a+1
# print(x(4))
# y = lambda a, b:a+b
# print(y(1,2))

def test(b):
    return lambda a:a*b

x = test(5)
print(x(6))

import requests
print(dir(requests))