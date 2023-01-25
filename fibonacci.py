def meth(n):
    
    if n==1 or n==2:
        sum = 1
    else:
        sum =  meth(n-1)+meth(n-2)
        
    return sum
    
x = meth(5)
print(x)