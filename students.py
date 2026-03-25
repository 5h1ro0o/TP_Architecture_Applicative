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

class Student:

    def __init__(self, name: str, grade1: float, grade2: float, grade3: float):
        self.__name = name
        self.__grades = [grade1, grade2, grade3]

    @property
    def name(self):
        return self.__name

    @property
    def grades(self):
        return self.__grades

    @property
    def average(self):
        return sum(self.__grades) / len(self.__grades)


class SchoolClass:

    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        self.__students.append(student)

    def rank_by_subject(self, subject_index: int):
        return sorted(self.__students, key=lambda s: s.grades[subject_index], reverse=True)

    def rank_by_average(self):
        return sorted(self.__students, key=lambda s: s.average, reverse=True)

    @property
    def students(self):
        return self.__students


if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    for i, subject in enumerate(['Matière 1', 'Matière 2', 'Matière 3']):
        print(f'\nClassement {subject}:')
        for student in school_class.rank_by_subject(i):
            print(f'  {student.name}: {student.grades[i]}')

    print('\nClassement par moyenne:')
    for student in school_class.rank_by_average():
        print(f'  {student.name}: {student.average:.2f}')