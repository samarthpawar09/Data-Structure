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
s1.insert(45)
s1.display()

            