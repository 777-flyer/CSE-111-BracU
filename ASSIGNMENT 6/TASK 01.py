class Student:

    ID = 0

    def __init__(self, name, department, age, cgpa):

        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.ID += 1
        self.id = Student.ID

    def showDetails(self):

        print(f'ID: {self.id}')
        print(f'Name: {self.name}')
        print(f'Department: {self.department}')
        print(f'Age: {self.age}')
        print(f"CGPA: {self.cgpa}")

    @classmethod
    def from_String(cls, string):

        name, department, age, cgpa = string.split("-")
        return cls(name, department, int(age), float(cgpa))


s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()
print("-----------------------")
s1.showDetails()

""" A class variable is a variable that is common to all  instances of a class, whereas an instance variable is 
specific to each instance of the class. """
