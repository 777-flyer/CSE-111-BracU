class Exam:

    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"

    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"


class ScienceExam(Exam):

    def __init__(self, marks, time, *subjects):
        super().__init__(marks)
        self.time = time
        self.subjects = list(subjects)

    def examSyllabus(self):
        return super().examSyllabus() + " , " + " , ".join(self.subjects)

    def examParts(self):
        parts = super().examParts()

        for i in range(len(self.subjects)):
            parts += f"Part {i + 3} - {self.subjects[i]}\n"

        return parts[:-1]

    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.subjects) + 2}"


engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())
