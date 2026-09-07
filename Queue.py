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
            y=self.QT[self.F]
        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1
        return y
    
    def display(self):
        if self.F==-1:
            print("Nothing to print..")
            return 
            for i in range(self.F,self.R+1):
                print(self.QT[i],end=" ")

q=Queue()
while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        x=int(input("Enter the element to insert: "))
        q.insert(x)

    elif choice==2:
        x=q.delete()
        if x is not None:
            print("Deleted element:",x)

    elif choice==3:
        q.display()

    elif choice==4:
        break

    else:
        print("Invalid choice..")
                
                
