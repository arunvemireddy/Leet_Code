x=-123
if(x<0):
    s=str(x)
    s=s[1:]
    s=s[::-1]
    s='-'+s
    x=int(s)
    print(x)