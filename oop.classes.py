# oop_classes.py

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}  # оценки за домашние задания

    def rate_lecture(self, lecturer, course, grade):
        """Студент ставит оценку лектору за курс"""
        if not isinstance(lecturer, Lecturer):
            print("Ошибка: оценивать можно только лектора")
            return "Ошибка"
        if course not in self.courses_in_progress:
            print(f"Ошибка: студент не записан на курс {course}")
            return "Ошибка"
        if course not in lecturer.courses_attached:
            print(f"Ошибка: лектор {lecturer.name} {lecturer.surname} не ведет курс {course}")
            return "Ошибка"
        if not (1 <= grade <= 10):
            print("Ошибка: оценка должна быть от 1 до 10")
            return "Ошибка"
        lecturer.grades.setdefault(course, []).append(grade)


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}  # оценки студентов по курсам


class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """Ревьюер ставит оценку студенту за домашку"""
        if not isinstance(student, Student):
            print("Ошибка: оценивать можно только студента")
            return "Ошибка"
        if course not in self.courses_attached or course not in student.courses_in_progress:
            print("Ошибка: курс не совпадает")
            return "Ошибка"
        if not (1 <= grade <= 10):
            print("Ошибка: оценка должна быть от 1 до 10")
            return "Ошибка"
        student.grades.setdefault(course, []).append(grade)


# -----------------------
# Пример использования
# -----------------------

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# Назначаем курсы
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

# Студент оценивает лектора
print(student.rate_lecture(lecturer, 'Python', 7))   # None, оценка успешно поставлена
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка: лектор не ведет этот курс
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка: студент не записан на курс
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка: можно оценивать только лектора

# Ревьюер оценивает студента
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'C++', 8)  # Ошибка: студент не записан на курс

# Проверяем оценки
print("Оценки лектора:", lecturer.grades)   # {'Python': [7]}
print("Оценки студента:", student.grades)   # {'Python': [9]}
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}  # оценки за домашние задания

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            print("Ошибка: оценивать можно только лектора")
            return "Ошибка"
        if course not in self.courses_in_progress:
            print(f"Ошибка: студент не записан на курс {course}")
            return "Ошибка"
        if course not in lecturer.courses_attached:
            print(f"Ошибка: лектор {lecturer.name} {lecturer.surname} не ведет курс {course}")
            return "Ошибка"
        if not (1 <= grade <= 10):
            print("Ошибка: оценка должна быть от 1 до 10")
            return "Ошибка"
        lecturer.grades.setdefault(course, []).append(grade)

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    # Операторы сравнения студентов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}  # оценки студентов по курсам

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}")

    # Операторы сравнения лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            print("Ошибка: оценивать можно только студента")
            return "Ошибка"
        if course not in self.courses_attached or course not in student.courses_in_progress:
            print("Ошибка: курс не совпадает")
            return "Ошибка"
        if not (1 <= grade <= 10):
            print("Ошибка: оценка должна быть от 1 до 10")
            return "Ошибка"
        student.grades.setdefault(course, []).append(grade)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    # -----------------------
    # Создание экземпляров
    # -----------------------

    # Студенты
    student1 = Student('Ольга', 'Алёхина', 'Ж')
    student2 = Student('Иван', 'Сидоров', 'М')

    # Лекторы
    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Мария', 'Петрова')

    # Ревьюеры
    reviewer1 = Reviewer('Пётр', 'Петров')
    reviewer2 = Reviewer('Анна', 'Смирнова')

    # -----------------------
    # Назначение курсов
    # -----------------------

    student1.courses_in_progress += ['Python', 'Java']
    student2.courses_in_progress += ['Python', 'C++']

    student1.finished_courses += ['Введение в программирование']
    student2.finished_courses += ['Введение в Python']

    lecturer1.courses_attached += ['Python', 'C++']
    lecturer2.courses_attached += ['Python', 'Java']

    reviewer1.courses_attached += ['Python', 'C++']
    reviewer2.courses_attached += ['Python', 'Java']

    # -----------------------
    # Оценивание
    # -----------------------

    # Студенты оценивают лекторов
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer2, 'Java', 8)
    student2.rate_lecture(lecturer1, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Python', 10)  # студент2 не на Python? проверим ошибки

    # Ревьюеры оценивают студентов
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student2, 'C++', 8)
    reviewer2.rate_hw(student1, 'Java', 7)
    reviewer2.rate_hw(student2, 'Python', 10)

    # -----------------------
    # Печать информации (__str__)
    # -----------------------

    print(student1)
    print(student2)
    print(lecturer1)
    print(lecturer2)
    print(reviewer1)
    print(reviewer2)

    # -----------------------
    # Функции для средней оценки по курсу
    # -----------------------

    def average_student_grade(students, course_name):
        """Средняя оценка всех студентов по курсу"""
        all_grades = []
        for student in students:
            if course_name in student.grades:
                all_grades.extend(student.grades[course_name])
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0

    def average_lecturer_grade(lecturers, course_name):
        """Средняя оценка всех лекторов по курсу"""
        all_grades = []
        for lecturer in lecturers:
            if course_name in lecturer.grades:
                all_grades.extend(lecturer.grades[course_name])
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 2)
        return 0

    # -----------------------
    # Проверка функций
    # -----------------------

    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]

    print("Средняя оценка студентов по Python:", average_student_grade(students_list, 'Python'))
    print("Средняя оценка студентов по Java:", average_student_grade(students_list, 'Java'))
    print("Средняя оценка лекторов по Python:", average_lecturer_grade(lecturers_list, 'Python'))
    print("Средняя оценка лекторов по Java:", average_lecturer_grade(lecturers_list, 'Java'))

    # -----------------------
    # Сравнение студентов и лекторов
    # -----------------------
    print("student1 > student2?", student1 > student2)
    print("lecturer1 < lecturer2?", lecturer1 < lecturer2)