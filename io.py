with open('sample.txt',"r") as f:
    f_contents = f.read(10)
    print(f_contents)
    while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(10)