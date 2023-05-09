class Student:

    def __init__(self, name, id_number, department="CSE"):

        self.name = name
        self.id = id_number
        self.department = department
        self.effort = 0

    def dailyEffort(self, hours):

        self.effort = hours

    def printDetails(self):

        two_hrs = "Should give more effort!"
        four_hrs = "Keep up the good work!"
        more_hrs = "Excellent! Now motivate others."

        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Department: {self.department}")
        print(f"Daily Effort: {self.effort}hour(s)")

        if self.effort in range(0, 3):
            print(f"Suggestion: {two_hrs}")
        elif self.effort in range(3, 5):
            print(f"Suggestion: {four_hrs}")
        elif self.effort > 4:
            print(f"Suggestion: {more_hrs}")


harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
