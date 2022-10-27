
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self,course_name):
        self.finished_courses.append(course_name)


    def rate_lecturer(self, lecturer, course, grades):
        """считает и записывает оценки лекторов: """
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grades]
            else:
                lecturer.lec_grades[course] = [grades]
        else:
            return 'Ошибка'
    

    def avarage_score(self):
        """считает среднюю оценку студента"""
        for value in self.grades.values():
            student_result = round(sum(value)/len(value))
            return student_result


    def __str__(self):
        """имя фамилия. Средняя студента. курсы в процессе """
        name_surname_grade = f' Имя: {self.name}'\
                             f"\n Фамилия: {self.surname}"\
                             f"\n Cредняя оценка студента: {self.avarage_score()}"\
                             f"\n Курсы в процессе изучения: {', ' .join(self.courses_in_progress)}"\
                             f"\n Завершенные курсы: {''.join(self.finished_courses)}"
        return name_surname_grade
    
    def __lt__(self, other):
        """сравнение между студентами"""
        if not isinstance(other, Student):
            print('сравнивать можно только студентов')
            return
        return self.avarage_score() > other.avarage_score()

class Mentor:
    """класс родитель"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
  
class Lecturer(Mentor):
    """класс лекторов"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}
        
        
    def avarage_score(self):
        for value in self.lec_grades.values():
            lecturer_result = round(sum(value)/len(value))
        return lecturer_result


    def __str__(self):
        """Имя. Фамилия. средняя оценка лекторов"""
        name_surname_grade = f" Имя: {self.name}"\
                             f"\n Фамилия: {self.surname}"\
                             f"\nсредняя оценка лектора: {self.avarage_score()}"
        return name_surname_grade
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'сравнивать можно только лекторов'
        return self.avarage_score() > other.avarage_score()

class Reviewer(Mentor):
    """инициализирует атрибуты класса Mentor.
    возвращяет имя фамилия ревьювера"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f" Имя ревьювера: {self.name}\n Фамилия: {self.surname}"
    

    def rate_hw(self, student, course, grade):
        """считает оценки студентов"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 




student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']

student_1 = Student('Sasha', 'Zhigulin', 'old')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['введение в програмирование']


reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 5)
reviewer.rate_hw(student, 'Python', 10)

reviewer_1 = Reviewer('No', 'buddy')
reviewer_1.courses_attached += ['Git', 'Python']
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 3)

lecturer = Lecturer('Олег', 'булыкин')
lecturer.courses_attached += ['Git']
lecturer_1 = Lecturer('Vitya', 'Tcoy')
lecturer_1.courses_attached += ['Git']

student.rate_lecturer(lecturer, 'Git', 7)
student.rate_lecturer(lecturer, 'Git', 3)
student.rate_lecturer(lecturer, 'Git', 10)

student_1.rate_lecturer(lecturer_1, 'Git', 5)
student_1.rate_lecturer(lecturer_1, 'Git', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 3)



print(student)
print(student.grades)
print()
print(student_1)
print(student_1.grades)
print(student > student_1)
print()
print(lecturer)
print(lecturer.lec_grades)
print(lecturer_1)
print(lecturer_1.lec_grades)
print(lecturer < lecturer_1)
print()
print(reviewer)
print(reviewer_1)


student_list = [student, student_1]

def all_student_score():
    git_score = []
    python_score = []
    for student in student_list:
        for subject, score in student.grades.items():
            if subject == 'Python':
                score_1 = round(sum(score)/len(score))
                python_score.append(score_1)
                return f"средняя оценка по Python у студентов: {python_score}"
            if subject == 'Git':
                score_2 = round(sum(score)/len(score))
                git_score.append(score_2)
                return f"средняя оценка по Gitу студентов: {git_score}"
print(all_student_score())

lecturer_list = [lecturer, lecturer_1]

def all_lecturer_score():
    git_score = []
    python_score = []
    for lecturer in lecturer_list:
        for subject, score in lecturer.lec_grades.items():
            if subject == 'Python':
                score_1 = round(sum(score)/len(score))
                python_score.append(score_1)
                return f"средняя оценка по Python у лекторов: {python_score}"
            if subject == 'Git':
                score_2 = round(sum(score)/len(score))
                git_score.append(score_2)
                return f"средняя оценка по Git у лекторов: {git_score}"
print(all_lecturer_score())