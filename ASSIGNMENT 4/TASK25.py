class Vaccine:

    def __init__(self, name, origin, waiting_period):

        self.name = name
        self.origin = origin
        self.waiting_period = waiting_period


class Person:

    def __init__(self, name, age, profession='General Citizen'):

        self.name = name
        self.age = age
        self.profession = profession

        self.vaccine_name = ''
        self.first_dose = False
        self.second_dose = False
        self.location = ''

    def pushVaccine(self, vaccine_name, dose='1st Dose'):

        if dose == '1st Dose':

            if self.age >= 25 or self.profession == 'Student':

                self.first_dose = True
                self.location = vaccine_name
                self.vaccine_name = self.location.name
                print(f'1st dose done for {self.name}')

            else:

                print(f'Sorry {self.name}, Minimum age for taking vaccines is 25 years now')

        else:

            if self.vaccine_name != vaccine_name.name:

                print(f"Sorry {self.name}, you can’t take 2 different vaccines")

            elif self.vaccine_name == vaccine_name.name and self.first_dose is True:

                self.second_dose = True
                print(f"2nd dose done for {self.name}")

    def showDetail(self):

        print(f"Name: {self.name} Age: {self.age} Type: {self.profession}")
        print(f"Vaccine Name: {self.vaccine_name}")

        if self.first_dose is True and self.second_dose is True:

            print("1st Dose: Given")
            print("2nd Dose: Given")

        elif self.first_dose is True and self.second_dose is False:

            print("1st Dose: Given")
            print(f"2nd Dose: Please come after {self.location.waiting_period} days")


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
