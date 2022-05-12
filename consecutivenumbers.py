

def method(num):
    res=0
    count=0
    i=1
    temp=0
    while i<int(num):
        if(res==0):
            temp=i
        res=res+i
        if res==num:
            res=0
            count=count+1
            i=temp+1
        if res<num:
            i=i+1
        if res>num:
            i=temp+1
            res=0
        

    print(count)
            
method(100)