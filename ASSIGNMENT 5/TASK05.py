class Student:

    def __init__(self, name, id_no, department):

        self.name = name
        self.id_number = id_no
        self.department = department
        self.email = None
        self.password = None
        self.login_status = None
        self.advised_courses = []

        print('Student object is created!')


class Usis:

    def __init__(self):

        print('USIS is ready to use!')

        self.current_students = []

    def login(self, student):

        if student.email is None and student.password is None:

            print("Email and Password need to be set.")

        else:

            student.login_status = True
            self.current_students.append(student)

            print("Login successful!")

    def advising(self, student, *courses):   # tuple

        if student.login_status is None:

            print("Please login to advise courses!")

        elif len(courses) == 0:

            print("You haven't selected any courses.")

        elif len(courses) > 3:

            print("You need special approval to take more than 3 courses.")

        else:

            student.advised_courses += list(courses)
            print("Advising Successful!")

    def individualDetails(self, student):

        if student in self.current_students:

            details = ''
            details += f'Name: {student.name}\n'
            details += f'ID: {student.id_number}\n'
            details += f'Department; {student.department}\n'
            details += f"Advised courses: {', '.join(student.advised_courses)}"

            return details


rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))
