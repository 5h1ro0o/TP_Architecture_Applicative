class Student:

    def init(self, name: str, grade1: float, grade2: float, grade3: float):
        self.name = name
        self.grades = [grade1, grade2, grade3]

    @property
    def name(self):
        return self.name

    @property
    def grades(self):
        return self.grades

    @property
    def average(self):
        return sum(self.grades) / len(self.grades)


class SchoolClass:

    def init(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    @property
    def students(self):
        return self.__students