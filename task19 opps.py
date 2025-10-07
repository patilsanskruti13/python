class Vehicle:
    def __init__(self, name):
        self.name = name
        self.seats = 0
        self.wheels = 0

    def get_details(self):
        self.seats=int(input(f"Enter the no. of seats {self.name} ="))
        self.wheels=int(input(f"Enter the no. of wheels in {self.name}="))
        
    def show(self):
        print(f"\n--- {self.name.upper()} DETAILS ---")
        print(f"Number of Seats: {self.seats}")
        print(f"Number of Wheels: {self.wheels}")
        
bus = Vehicle("Bus")
car = Vehicle("Car")
truck = Vehicle("Truck")
auto = Vehicle("Auto")


bus.get_details()
car.get_details()
truck.get_details()
auto.get_details()


bus.show()
car.show()
truck.show()
auto.show()