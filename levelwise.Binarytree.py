class Node:
    def __init__(self, data):
        self.left= None
        self.right = None
        self.data = data

def insert(root,x):
    if root==None:
        return Node(x)
    if root.data<x:
        root.right=insert(root.right,x)
    else: 
        root.left=insert(root.left,x)
    return root

def create():
    root=None
    while True:
        x=int(input("Enter data to create node(0 to stop):"))
        if x==0:
            break
        else:
            root=insert(root,x)
    return root

#recursive inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

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
            return None
        else:
            y=self.QT[self.F]

        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1
        return y

def level_wise(root):

    if root is None:
        return
    q=Queue()
    q.insert(root)

    while q.F!=-1:
        r=q.delete()
        print(r.data,end="")
   

        if r.left is not None:
            q.insert(r.left)
        if r.right is not None:
            q.insert(r.right)

    
r=create()
inorder(r)
print("Level wise is:")
level_wise(r)
