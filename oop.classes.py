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