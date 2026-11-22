class Graph:
    def __init__(self,v):
        self.vertices=v
        self.AdjL=[[]for i in range(v)]

    def addEdge(self):
        e=int(input("Enter no of edges:"))

        for i in range(e):
            print(("Enter Edge(i+1)"))
            u=int(input("Enter start vertex:"))
            v=int(input("Enter end vertex:"))
            self.AdjL[u].append(v)
            self.AdjL[v].append(u)

    def display(self):
        for i in range (self.vertices):
            print(i,"->",self.AdjL[i])

    def bfs(self,start):
        visited=[False]*self.vertices
        q=Queue()
        q.insert(start)
        visited[start]=True

        while q.F!=-1:
            current=q.delete()
            print(current)

            for vertex in self.AdjL[current]:
                 if visited[vertex]==False:
                     visited[vertex]=True
                     q.insert(vertex)
          


class Queue:
    def __init__(self):
        self.F=-1
        self.R=-1
        self.QT=[0]*5

    def insert(self,x):
        if self.R==4:
            print("Queue is overflow..")
            return
        self.R=self.R+1
        self.QT[self.R]=x
        if self.F==-1:
            self.F=0

    def delete(self):
        if self.F==-1:
            print("Nothing to print..")
            return
        else:
            x=self.QT[self.F]
        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1
        return x        
ob=Graph(3)
ob.addEdge()
ob.display()
start=int(input("Enter the start vertex:"))
ob.bfs(start)
