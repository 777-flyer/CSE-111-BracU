class Student:

    def __init__(self, name="default student"):
        self.name = name
        self.quizzes = []

    def quizcalc(self, *scores):
        self.quizzes = scores[:3]

    def printdetail(self):
        average_score = sum(self.quizzes) / 3
        print(f"Hello {self.name}")
        print(f"Your average quiz score is {average_score}")


s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10, 8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10, 9, 10)
print('--------------------------------')
s3.printdetail()
