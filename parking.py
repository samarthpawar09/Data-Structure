class ParkingGarage:
    def __init__(self):
        self.stack = []
        self.max_size = 10

    def park_vehicle(self, reg_no, vehicle_type):
        if len(self.stack) >= self.max_size:
            print("Parking Garage is Full!")
            return

        if vehicle_type not in ["Car", "Bike"]:
            print("Only Car and Bike are allowed!")
            return

        for vehicle in self.stack:
            if vehicle[0] == reg_no:
                print("Duplicate Registration Number not allowed!")
                return

        self.stack.append((reg_no, vehicle_type))
        print("Vehicle Parked Successfully.")

    def exit_vehicle(self):
        if not self.stack:
            print("Parking Garage is Empty!")
        else:
            print("Exited Vehicle:", self.stack.pop())

    def top_vehicle(self):
        if not self.stack:
            print("Parking Garage is Empty!")
        else:
            print("Top Vehicle:", self.stack[-1])

    def display(self):
        if not self.stack:
            print("No Vehicles Parked.")
        else:
            print("\nParked Vehicles (Top to Bottom):")
            for vehicle in reversed(self.stack):
                print(vehicle)

garage = ParkingGarage()

while True:
    print("\n1. Park Vehicle")
    print("2. Exit Vehicle")
    print("3. Top Vehicle")
    print("4. Display Parked Vehicles")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        reg_no = input("Enter Registration Number: ")
        vehicle_type = input("Enter Vehicle Type (Car/Bike): ")
        garage.park_vehicle(reg_no, vehicle_type)

    elif choice == 2:
        garage.exit_vehicle()

    elif choice == 3:
        garage.top_vehicle()

    elif choice == 4:
        garage.display()

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")