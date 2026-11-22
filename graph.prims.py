class Graph:
    def __init__(self):
        self.v=0
        self.e=0
        self.G=[]
    def create(self):
        self.v=int(input("Enter no of vertices:"))
        self.e=int(input("Enter no of edges:"))
        self.G=[[0 for i in range(self.v)] for j in range(self.v)]

        for i in range(self.e):
            print(f"\nEnter edge{i+1}")
            u=int(input("Enter start vertex: "))
            v=int(input("Enter end vertex: "))
            w=int(input("Enter weight: "))
            self.G[u][v]=w
            self.G[v][u]=w

    def display(self):
        for i in range (self.v):
            for j in range (self.v):
               print(self.G[i][j],end=" ")
            print()
    def prims(self):
        selected=[False]*self.v 
        key=[999]*self.v
        parent=[-1]*self.v
        key[0]=0

        for i in range (self.v):
            min_weight=999
            u=-1
            for j in range (self.v):
                if(selected[j]==False and key[j]<min_weight):
                    min_weight=key[j]
                    u=j
            selected[u]=True
            for v in range(self.v):
                 if(self.G[u][v]!=0 and selected[v]==False and self.G[u][v]<key[v]):
                    key[v]=self.G[u][v]
                    parent[v]=u
        total=0
        for i in range(1,self.v):
            print(parent[i],"-",i,self.G[i][parent[i]])
            total=total+self.G[i][parent[i]]
        print("Total cost",total)
ob=Graph()
ob.create()
ob.display()    
ob.prims()


        