class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
    
    def create(self):
        n=int(input("Enter no of node"))

        if n<=0:
            print("Enter the valid no of node ")
            return 
        for n in range(1,n+1):
            val=input(f"Enter data for node{n}:")
            self.insert(val)

    def insert (self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            return 
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def show(self):
        if self.head==None:
            print("Nothing to print")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next

    def delete(self,val):
        if self.head is None:
            print("linked list is Empty")
            return 
        if self.head.data==val:
            self.head=self.head.next
            print("Node deleted")
            return
        
        temp=self.head 

        while temp.next is not None and temp.next.datd!=val:
            temp=temp.next

        if temp.next is None:
            print("Node not found")
        else:
            temp.next=temp.next.next
            print("Node deleted")

s1=LL()
while True:

    print("\n1.Create linked list")
    print("2.Show")
    print("3.delete")
    print("4.Exit")
    choice =int(input("Enter your choice"))

    if choice ==1:
        s1.create()
    if choice ==2:
        s1.show()
    if choice ==3:
        s1.delete()
    if choice ==4:
        break
    

   



