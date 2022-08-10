from statistics import mean

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade(self)}\nКурсы в процессе изучения: {str(self.courses_in_progress)[1:-1]}\nЗавершенные курсы: {str(self.finished_courses)[1:-1]}'
        return res

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return avg_grade(self) < avg_grade(other)

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture,
                      Lecture) and course in self.courses_in_progress and course in lecture.courses_attached and 0 <= int(
            grade) <= 10:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return "Ошибка"


class Lecture(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade(self)}'
        return res
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __lt__(self, other):
        if not isinstance(other, Lecture):
            print('Not a Lecture!')
            return
        return avg_grade(self) < avg_grade(other)

class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and 0 <= int(
            grade) <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def avg_grade(self):
    result = []
    if len(self.grades) > 0:
        for i in self.grades:
            result += self.grades[i]
        result = (int(x) for x in result)
        return round(mean(result), 1)
    else:
        return ""

reviewer_alex = Reviewer("Alexey", "Zazulya")
reviewer_platon = Reviewer("Platon", "Markov")
lector_serg = Lecture("Sergey", "Nazarov")
lector_pavel = Lecture("Pavel", "Beliy")
student_vasiliy = Student("Vasiliy", "Gordeev", "m")
student_petr = Student("Petr", "Goncharov", "m")

print(student_vasiliy, "\n")
print(lector_serg, "\n")
print(reviewer_alex, "\n")