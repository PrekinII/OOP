class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_hw(self, lecturer, course, grade):  # Метод оценки лекторов
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress and grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self):  # Подсчет среднего балла
        m_grade = 0
        for grade in self.grades.values():
            m_grade += sum(grade) / len(grade) / len(self.grades)
        return m_grade

    def __str__(self):  # Переопределение __str_
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.middle_grade()}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):  # Оператор сравнения
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.middle_grade() < other.middle_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def middle_grade(self):  # Подсчет среднего балла за лекции
        m_grade = 0
        for grade in self.grades.values():
            m_grade += sum(grade) / len(grade) / len(self.grades)
        return m_grade

    def __str__(self):  # Переопределение __str_
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.middle_grade()}')
        return res

    def __lt__(self, other):  # Оператор сравнения
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.middle_grade() < other.middle_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):  # Оценка студентов только у reviewer
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # Переопределение __str_
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Ivan', 'Prekin', 'male')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Java']
best_student2.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Mentor('Some 2', 'Buddy 2')
cool_mentor2.courses_attached += ['Java']

cool_reviewer = Reviewer('Alexandr', 'Bardin')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 5)
cool_reviewer.rate_hw(best_student2, 'Python', 9)

cool_reviewer2 = Reviewer('Some_reviewer', 'Buddy_reviewer')
cool_reviewer2.courses_attached += ['Java']
cool_reviewer2.courses_attached += ['Python']
cool_reviewer2.rate_hw(best_student2, 'Python', 9)

cool_lecturer = Lecturer('Elena', 'Nikitina')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

cool_lecturer2 = Lecturer('Oleg', 'Bulygin')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Java']

best_student.lecturer_hw(cool_lecturer, 'Python', 10)
best_student2.lecturer_hw(cool_lecturer, 'Python', 7)
best_student.lecturer_hw(cool_lecturer, 'Java', 9)
best_student2.lecturer_hw(cool_lecturer, 'Java', 6)

best_student.lecturer_hw(cool_lecturer2, 'Python', 10)
best_student2.lecturer_hw(cool_lecturer2, 'Python', 10)
best_student.lecturer_hw(cool_lecturer2, 'Java', 9)
best_student2.lecturer_hw(cool_lecturer2, 'Java', 9)

all_students = [best_student, best_student2]  # Создаем список студентов и лекторов
all_lecturers = [cool_lecturer, cool_lecturer2]

def all_middle_grades(all_pers): # Создаем функцию для расчета среднего общего балла
    all_m_grade = 0
    for pers in all_pers:
        all_m_grade += pers.middle_grade()
    print(f'Общий средний балл: {all_m_grade / len(all_pers)}')
    return

all_middle_grades(all_students)
all_middle_grades(all_lecturers)

print(best_student.grades)
print(best_student2.grades)

print(cool_lecturer.grades)
print(len(cool_lecturer.grades.values()))
print(cool_lecturer2.grades)

print(cool_reviewer)
print(cool_lecturer)
print(cool_lecturer2)
print(best_student)
print(best_student2)

print(best_student > best_student2)

print(cool_lecturer > cool_lecturer2)

print(cool_reviewer)
print(cool_lecturer)
print(cool_lecturer2)
print(best_student)
print(best_student2)

print(best_student > best_student2)

print(cool_lecturer > cool_lecturer2)
