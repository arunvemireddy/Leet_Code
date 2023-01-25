class PallindromeString:

    def __init__(self):
        s = input()
        z = self.meth1(s)
        if s == z:
            print("pallindrome")
        else:
            print("is not pallindrome")

    def meth1(self,x):
        y = ''
        for i in x[::-1]:
            y = y+i
        return y

obj = PallindromeString()
