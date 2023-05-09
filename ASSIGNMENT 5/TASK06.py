class Train:

    def __init__(self, name, *stops):

        self.name = name
        self.stops = list(stops)
        self.passengers = []

        print(f"Welcome to {self.name}")
        print(f"Start: {self.stops[0]}")
        print(f"Destination: {self.stops[-1]}")

    def addPassenger(self, *passengers):

        for p in passengers:

            if p.start not in self.stops:
                p.start = self.stops[0]

            if p.destination not in self.stops:
                p.destination = self.stops[-1]

            self.passengers.append(p)

        for g in range(len(passengers)):
            print(f"{passengers[g].name} welcome abroad")

    def allPassengerDetails(self):

        for p in self.passengers:
            start_index = self.stops.index(p.start)
            destination_index = self.stops.index(p.destination)
            fare = abs(start_index - destination_index) * 100
            print(f"Name: {p.name},Start: {p.start},Destination: {p.destination},Fair: ${fare}")


class Passenger:

    def __init__(self, name, start=None, destination=None):
        self.name = name
        self.start = start
        self.destination = destination


t1 = Train('T1-Express', 'New York', 'Manhattan', 'Brooklyn', 'Boston')
print("1========================")
p1 = Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke", "Manhattan")
p3 = Passenger("Hinata", "Manhattan", "Brooklyn")
print("2========================")
t1.addPassenger(p2, p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express', 'London', 'Paris', 'Brussels', 'Turkey')
print("5========================")
p4 = Passenger("Max", "London", "Brussels")
p5 = Passenger("Eleven", "Paris")
p6 = Passenger("Mike", "Brussels")
t2.addPassenger(p4, p5, p6)
print("6========================")
t2.allPassengerDetails()
