class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
        n=int(input("Enter data to create the node (o to stop):"))
        if n==0:
            return None 
        root = Node(n)
        print (f"enter left of {n}:")
        root.left=create()
        print(f"enter right of {n}:")
        root.right=create()
        return root 

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder (root.left)
        preorder(root.right)

def inorder(root):
     if root is not None:
          inorder (root.left)
          print(root.data, end=" ")
          inorder(root.right)

def postorder(root):
     if root is not None:
          postorder(root.left)
          postorder(root.right)
          print(root.data , end=" ")


root=create()

print("preorder traversal")
preorder(root)

print("inoder traversal")
inorder(root)

print("postorder traversal")
postorder(root)
