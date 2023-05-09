class Employee:

    def __init__(self, name, workingPeriod):

        self.name = name
        self.workingPeriod = workingPeriod

    @classmethod
    def employeeByJoiningYear(cls, name, year):

        current_year = 2023
        working_period = current_year - year
        return cls(name, working_period)

    @staticmethod
    def experienceCheck(working_period, gender):

        if working_period < 3:

            return "He is not experienced" if gender == "male" else "She is not experienced"

        else:

            return "He is experienced" if gender == "male" else "She is experienced"


employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))
