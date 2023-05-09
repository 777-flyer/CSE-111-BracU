class Travel:

    count = 0
    base_fly_time = 1

    def __init__(self, source, destination):

        self.source = source
        self.destination = destination
        self.fly_time = self.base_fly_time
        Travel.count += 1

    def set_source(self, source):

        self.source = source

    def set_destination(self, destination):

        self.destination = destination

    def set_time(self, fly_time):

        self.fly_time = fly_time

    def display_travel_info(self):

        return f"Source: {self.source}\nDestination:{self.destination}\nFlight Time:{self.fly_time: 02d}:00"


print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka", "India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur", "Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka", "New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka", "India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)
