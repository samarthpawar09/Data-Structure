class Stack:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    # Push - Return a book
    def push(self):
        book = input("Enter book name: ")
        new_node = Stack(book)

        new_node.next = self.head
        self.head = new_node

        print("Book returned successfully")

    # Pop - Process returned book
    def pop(self):
        if self.head is None:
            print("Stack is Empty")
            return

        book = self.head.data
        self.head = self.head.next

        print("Book processed:", book)

    # Display stack
    def show(self):
        if self.head is None:
            print("No returned books")
            return

        temp = self.head
        print("Returned books:")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


s1 = LL()

while True:

    print("\n1. Return Book")
    print("2. Process Book")
    print("3. Show Returned Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s1.push()

    elif choice == 2:
        s1.pop()

    elif choice == 3:
        s1.show()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid choice")