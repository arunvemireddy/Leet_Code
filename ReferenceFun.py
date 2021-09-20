class pyRef:
    def meth1(self):
        x=-2.56
        x=abs(x)
        print(x)

    def meth2(self):
        x = dict(name="arun",age="23",country="india")

        print(x["name"])

        y={"name":"ravi","age":"30"}

        print(y["name"]+""+y["age"])

        z={"name":"mango"}

        print(z.get("name"))

        m={"name":"ball","sports":"cricket"}

        print(m.keys())

        m["color"]="red"

        print(m)
        print(m.values())
        m["color"]="yellow"
        print(m.values())


    
        
p = pyRef()

p.meth1()
p.meth2()

print(id(p))