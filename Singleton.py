class Singleton:
    instance=None
    @staticmethod
    def getInstance():
        if Singleton.instance==None:
            Singleton()
        return Singleton.instance

    def __init__(self):
        if Singleton.instance!=None:
            raise Exception("This Class is not singleton")
        else:
            Singleton.instance=self


s = Singleton.getInstance()

print(s)

s = Singleton()
print (s)



s= Singleton.getInstance()
print(s)