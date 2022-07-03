import thread
from threading import Thread

def meth1(k,j):
    print(k)
    print(j)

t=Thread(target=meth1,args=("arun","kumar"))
t.start()
