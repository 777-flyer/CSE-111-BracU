class Student:

    def __init__(self, name=None, department=None):

        self.name = name
        self.department = department
        self.courses = []

        if self.name is None and self.department is None:

            print("Student name and department need to be set.")

        elif self.name is not None and self.department is None:

            print(f"Department for {self.name} needs to be set.")

        elif self.name is not None and self.department is not None:

            print(f"{self.name} is from {self.department} department.")

    def update_name(self, new_name):

        self.name = new_name

    def update_department(self, new_department):

        self.department = new_department

    def enroll(self, *course_name):

        self.courses += list(course_name)

    def printDetail(self):

        print("Name: {}".format(self.name))
        print(f"department: {self.department}")

        number_of_courses = len(self.courses)

        print(f"{self.name} is enrolled in {number_of_courses} course(s):")
        print(", ".join(self.courses))


s1 = Student()
print("=========================")
s2 = Student("Carol")
print("=========================")
s3 = Student("Jon", "EEE")
print("=========================")
s1.update_name("Bob")
s1.update_department("CSE")
s2.update_department("BBA")
s1.enroll("CSE110", "MAT110", "ENG091")
s2.enroll("BUS101")
s2.enroll("CSE230")
s2.enroll("CSE111")
s2.enroll("MAT120")
s3.enroll("MAT110", "PHY111")
print("###########################")
s1.printDetail()
print("=========================")
s2.printDetail()
print("=========================")
s3.printDetail()
'''
Student name and department need to be set
=========================
Department for Carol needs to be set
=========================
Jon is from EEE department
=========================
###########################
Name: Bob
Department: CSE
Bob enrolled in 3 course(s):
CSE110, MAT110, ENG091
=========================
Name: Carol
Department: BBA
Carol enrolled in 1 course(s):
BUS101
=========================
Name: Jon
Department: EEE
Jon enrolled in 2 course(s):
MAT110, PHY111

'''
