class Queue:
    def __init__(self):
        self.F = -1
        self.R = -1
        self.QT = [0] * 5

    def insert(self, x):
        if self.R == 4:
            print("Queue is overflow..")
            return

        if self.F == -1:
            self.F = 0

        self.R = self.R + 1
        self.QT[self.R] = x
        print("Ticket booked:", x)

    def delete(self):
        if self.F == -1:
            print("Queue is underflow..")
            return

        y = self.QT[self.F]

        if self.F == self.R:
            self.F = self.R = -1
        else:
            self.F = self.F + 1

        print("Ticket processed:", y)

    def display(self):
        if self.F == -1:
            print("Queue is empty..")
            return

        print("Tickets in queue:")
        for i in range(self.F, self.R + 1):
            print(self.QT[i])


q = Queue()

while True:

    print("\n1. Book Ticket")
    print("2. Process Ticket")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ticket = input("Enter passenger name: ")
        q.insert(ticket)

    elif choice == 2:
        q.delete()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice")