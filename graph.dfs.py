class Graph:
    def __init__(self):
        self.v=0
        self.e=0
        self.G=[[0 for i in range(9)] for j in range(9)]
    def create(self):
        self.v=int(input("Enter no of vertices:"))
        self.e=int(input("Enter no of edges:"))

        for i in range(self.e):
            print(f"Enter edges(i+1):")
            u=int(input("Enter start vertex:"))
            v=int(input("Enter end vertex:"))
            w=int(input("Enter weight:"))
            self.G[u][v]=self.G[v][u]=w
            #self.G[u][v]=1 directed non weighted

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j],end=" ")
            print()
class Stack:
    def __init__(self):
        self.top=-1
        self.ST=[0]*100

    def push(self,x):
        if self.top==99:
            print("Stack is overflow..")
            return
        else:
            self.top=self.top+1
            self.ST[self.top]=x

    def pop(self):
        if self.top==-1:
            print("Nothing to print..")
            return
        else:
            x=self.ST[self.top]
            self.top=self.top-1
        return x

def dfs(ob, v):
        visited=[False]*ob.v
        s=Stack()
        s.push(start)
        while s.top!=-1:
            u=s.poo()
            if visited[u]==False:
                print(u,end=" ")
                visited[u]=True
            for i in range (ob.v-1,-1,-1):
                if(ob.G[u][v]!=0 and visited[v]==False):
                    s.push(v)



ob=Graph()
ob.create()
ob.display()
start=int(input("Enter start vertex:"))
dfs(ob,start)


  