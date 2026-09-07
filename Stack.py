class Stack:
    def __init__(self):
        self.top=-1
        self.ST=[0]*7

    def insert(self,x):
        if self.top==6:
            print("Stack is overflow..")
            return
        self.top=self.top+1
        self.ST[self.top]=x

    def delete(self):
        if self.top==-1:
            print("Nothing to print..")
            return
        else:
            y=self.ST[self.top]
            self.top=self.top-1
        return y
    
    def display(self):
        if self.top==-1:
            print("Nothing to print..")
            return 
        else: 
            for i in range(self.top,-1,-1):
                print(self.ST[i])
                return self.ST[i]

s1= Stack()
while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        x=int(input("Enter element to insert: "))
        s1.insert(x)
    elif choice==2:
        x=s1.delete()
        if x is not None:
            print("Deleted element is:",x)
    elif choice==3:
        s1.peek()
    elif choice==4:
        s1.display()
    elif choice==5:
        break


            

            
