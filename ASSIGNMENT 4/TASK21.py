# Write your code here

class Student:

    def __init__(self, name, id_number, department):

        self.name = name
        self.id_number = id_number
        self.department = department
        self.courses = []

    def advise(self, *course_names):

        self.courses += list(course_names)

        total_courses = len(self.courses)
        total_credits = (total_courses * 3.0)

        print(f'{self.name}, you have taken {total_credits} credits.')
        print("List of courses: {}".format(", ".join(self.courses)))

        status = ""

        if total_courses == 3 or total_courses == 4:
            status = "Ok"
        elif total_courses > 4:
            status = "You have to drop at least 1 course."
        elif total_courses < 3:
            status = "You have to take at least 1 more course."
        elif total_courses > 5:
            status = "It requires permission from the Office of the Registrar to take more than 5 courses."
        print(f'Status: {status}')

    def details(self):

        return f"Name: {self.name} \nID: {self.id_number} \nDepartment: {self.department}"


# Do not change the following lines of code.
s1 = Student("Alice", "20103012", "CSE")
s2 = Student("Bob", "18301254", "EEE")
s3 = Student("Carol", "17101238", "CSE")
print("##########################")
print(s1.details())
print("##########################")
print(s2.details())
print("##########################")
s1.advise("CSE110", "MAT110", "PHY111")
print("##########################")
s2.advise("BUS101", "MAT120")
print("##########################")
s3.advise("MAT110", "PHY111", "ENG102", "CSE111", "CSE230")

'''
##########################
Name: Alice
ID: 20103012
Department: CSE
##########################
Name: Bob
ID: 18301254
Department: EEE
##########################
Alice, you have taken 9.0 credits.
List of courses: CSE110, MAT110, PHY111
Status: Ok
##########################
Bob, you have taken 6.0 credits.
List of courses: BUS101, MAT120
Status: You have to take at least 1 more course.
##########################
Carol, you have taken 15.0 credits.
List of courses: MAT110, PHY111, ENG102,
CSE111, CSE230
Status: You have to drop at least 1 course.
'''
