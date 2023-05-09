class BracuStudent:

    def __init__(self, name, home):

        self.name = name
        self.home = home
        self.has_bus_pass = False

    def show_details(self):

        print(f"Student Name: {self.name}\nLives in {self.home}\nHave Bus Pass? {self.has_bus_pass}")

    def get_pass(self):

        self.has_bus_pass = True


class BracuBus:

    def __init__(self, route, max_capacity=2):

        self.route = route
        self.passengers = []
        self.max_capacity = max_capacity

    def show_details(self):

        print(f"Bus Route: {self.route}")
        print(f"Passengers Count: {len(self.passengers)} (Max: {self.max_capacity})")
        print(f"Passengers On Board: {self.passengers}")

    def board(self, *students):

        if len(students) == 0:

            print("No passenger!")

        else:

            for s in students:

                if not s.has_bus_pass:

                    print("You don't have bus pass!")

                elif s.home != self.route:

                    print("You got on wrong bus!")

                elif len(self.passengers) >= self.max_capacity:

                    print("Bus is full!")

                else:

                    self.passengers.append(s.name)
                    print(f"{s.name} boarded the bus.")


st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
