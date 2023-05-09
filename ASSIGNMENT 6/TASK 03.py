class Passenger:

    base_fare = 450
    passenger_count = 0

    def __init__(self, name):

        self.name = name
        self.bag_weight = 0
        Passenger.passenger_count += 1

    def set_bag_weight(self, weight):

        self.bag_weight = weight

    def get_bus_fare(self):

        fare = Passenger.base_fare

        if self.bag_weight in range(21, 51):

            fare += 50

        elif self.bag_weight > 50:

            fare += 100

        return fare

    def printDetail(self):

        print(f"Name: {self.name}")
        print(f"Bus fare: {self.get_bus_fare()} Taka")


print("Total Passenger:", Passenger.passenger_count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.passenger_count)
