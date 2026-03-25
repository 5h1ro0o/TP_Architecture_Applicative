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

    def rank_matter_1(self):
        return sorted(self.__students, key=lambda s: s.grades[0], reverse=True)

    def rank_matter_2(self):
        return sorted(self.__students, key=lambda s: s.grades[1], reverse=True)

    def rank_matter_3(self):
        return sorted(self.__students, key=lambda s: s.grades[2], reverse=True)

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

    print('\nClassement Matière 1:')
    for student in school_class.rank_matter_1():
        print(f'  {student.name}: {student.grades[0]}')

    print('\nClassement Matière 2:')
    for student in school_class.rank_matter_2():
        print(f'  {student.name}: {student.grades[1]}')

    print('\nClassement Matière 3:')
    for student in school_class.rank_matter_3():
        print(f'  {student.name}: {student.grades[2]}')

    print('\nClassement par moyenne:')
    for student in school_class.rank_by_average():
        print(f'  {student.name}: {student.average:.2f}')