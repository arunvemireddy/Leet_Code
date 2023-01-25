class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key == data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    def dispay(self):
        value = self
        while value is not None:
            print(value.key)
            value=value.lchild

        # value = self.rchild
        while value is not None:
            print(value.key)
            value=value.rchild

root = BST(None)
list1 = [30,5,10,40,70]
print(list1)
for i in list1:
    root.insert(i)

root.dispay()