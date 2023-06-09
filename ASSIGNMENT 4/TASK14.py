class StudentDatabase:

    def __init__(self, name, id_number):

        self.name = name
        self.id_number = id_number
        self.grades = {}

    def calculateGPA(self, courses, semester):

        course_list = []
        gpa = 0

        for course in courses:

            course_name, grade = course.split(": ")
            course_list.append(course_name)
            gpa += float(grade)

        number_of_courses = len(course_list)
        number_of_credits = number_of_courses * 3
        cgpa_calculation = (gpa * 3) / number_of_credits
        cgpa = round(cgpa_calculation, 2)

        if semester in self.grades:

            self.grades[semester][tuple(course_list)] = cgpa

        else:

            self.grades[semester] = {tuple(course_list): cgpa}

    def printDetails(self):

        print(f"Name: {self.name}")
        print(f"ID: {self.id_number}")

        for semester, courses in self.grades.items():

            print(f"Course taken in {semester}:")

            for course_name, cgpa in courses.items():

                for name in course_name:
                    print(name)
                print(f"GPA: {cgpa}")


s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()
