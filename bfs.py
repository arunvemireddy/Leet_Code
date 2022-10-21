class bfs:
    def meth1(self,n,edges):
        preMap = {i:[] for i in range(n)}
        x=type(preMap)
        print(x)
        for i, j in edges:
            preMap[i].append(j)
            preMap[j].append(i)
        visited= set()
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for n in preMap[i]:
                dfs(n)
            return True
        result=0
        print(preMap)
        for i in preMap:
            if dfs(i):
                result+=1
        return result

obj = bfs()
x=obj.meth1(5,[[0,1],[1,2],[2,0],[3,4]]) 
print(x)

my_dict=[{'s':1,'t':2},
        {'s':2,'t':3},
        {'s':3,'t':1},
        {'s':4,'t':5},
        {'s':5,'t':6},
        {'s':6,'t':4}]


output=[{'s':1,'t':2,'id':1},
        {'s':2,'t':3,'id':1},
        {'s':3,'t':1,'id':1},
        {'s':4,'t':5,'id':2},
        {'s':5,'t':6,'id':2},
        {'s':6,'t':4,'id':2}]