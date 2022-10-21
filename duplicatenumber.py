


def method(arr):
    narr = set(arr)
    temp=0

    seen = set()
    dupes = []

    for x in arr:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)

    print(dupes[0])

    for i in range(1,len(arr)):
    
        if i not in arr:
            temp=i
    
    print(temp+dupes[0])

arr=[4,3,3,1]
method(arr)