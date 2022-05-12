


s = "PAYPALISHIRING"
numRows = 4
nl=[]
for i in s:
    nl.append(i)

ll=numRows
j=len(nl)
for i in range(0,j):
    f=2*(ll-i)-(2-i)
    if(nl[f]):
        nl[i]=nl[i]+nl[f]
        nl.pop(f)
        j=len(nl)
    


print(nl)


