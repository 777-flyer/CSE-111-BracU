class Cat:

    Number_of_cats = 0

    def __init__(self, color='White', activity="sitting"):

        self.color = color
        self.activity = activity
        Cat.Number_of_cats += 1

    @classmethod
    def no_parameter(cls):

        return cls()

    @classmethod
    def first_parameter(cls, color):

        return cls(color)

    @classmethod
    def second_parameter(cls, activity):

        return cls(activity=activity, color="Grey")

    def printCat(self):

        print(f"{self.color} cat is {self.activity}")

    def changeColor(self, newColor):

        self.color = newColor


print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
