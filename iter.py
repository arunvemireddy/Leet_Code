mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

for i in range(len(mytuple)):
    try:
        print(next(myit))
        print(next(myit))
        print(next(myit))
        print(next(myit))
    except:
        break

x={"name":"arun","age":"24","school":"USU"}
for i,j in enumerate(x):
    print(i)
    