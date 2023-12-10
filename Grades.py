class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached):

            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return 'Ошибка'

    def av_rating(self):
         grades_count = 0
         for grade in self.grades:
            grades_count += len(self.grades[grade])
         result = sum(map(sum, self.grades.values())) / grades_count

         return result

    def av_rating_course(self, course):
        sum_course = 0
        len_course = 0
        for name_ in self.grades.keys():
            if name_ == course:
                sum_course += sum(self.grades[course])
                len_course += len(self.grades[course])
        result = round(sum_course / len_course, 2)
        return result

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание:{self.av_rating()}\n' \
              f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}'

        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return

        return self.av_rating > other.av_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}
        self.av_rating_lec = []

    def __str__(self):
        grades_count = 0
        for grade in self.grades_lec:
            grades_count += len(self.grades_lec[grade])
            self.av_rating= round((sum(map(sum, self.grades_lec.values())) / grades_count), 2)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating}'
        return res

    def av_rating_course(self, course):

        sum_course = 0
        len_course = 0
        for name_ in self.grades_lec.keys():
            if name_ == course:
                sum_course += sum(self.grades_lec[course])
                len_course += len(self.grades_lec[course])
        result = round(sum_course / len_course, 2)
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.av_rating > other.av_rating


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_stu(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lecturer_1 = Lecturer('Left', 'Pelmen')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Vasa', 'Mad')
lecturer_2.courses_attached += ['Git']

lecturer_3 = Lecturer('Otto', 'Octavius')
lecturer_3.courses_attached += ['Git', 'Python']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Lilly', 'White')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

student_1 = Student('Wedhes', 'Day')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование', '']

student_2 = Student('Roman', 'Babayan')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Leader', 'Goat')
student_3.courses_in_progress += ['Python', 'Git']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_2, 'Git', 5)
student_1.rate_lec(lecturer_2, 'Git', 7)
student_1.rate_lec(lecturer_2, 'Git', 8)
student_1.rate_lec(lecturer_3, 'Python', 7)
student_1.rate_lec(lecturer_3, 'Python', 8)
student_1.rate_lec(lecturer_3, 'Python', 9)

student_2.rate_lec(lecturer_2, 'Git', 10)
student_2.rate_lec(lecturer_2, 'Git', 8)
student_2.rate_lec(lecturer_2, 'Git', 9)

student_3.rate_lec(lecturer_3, 'Python', 5)
student_3.rate_lec(lecturer_3, 'Git', 6)
student_3.rate_lec(lecturer_3, 'Python', 7)

reviewer_1.rate_hw_stu(student_1, 'Python', 8)
reviewer_1.rate_hw_stu(student_1, 'Git', 9)
reviewer_1.rate_hw_stu(student_1, 'Python', 10)

reviewer_2.rate_hw_stu(student_2, 'Python', 8)
reviewer_2.rate_hw_stu(student_2, 'Git', 7)
reviewer_2.rate_hw_stu(student_2, 'Python', 9)

reviewer_2.rate_hw_stu(student_3, 'Python', 8)
reviewer_2.rate_hw_stu(student_3, 'Python', 7)
reviewer_2.rate_hw_stu(student_3, 'Git', 9)
reviewer_2.rate_hw_stu(student_3, 'Git', 8)
reviewer_2.rate_hw_stu(student_3, 'Python', 7)
reviewer_2.rate_hw_stu(student_3, 'Python', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')

print()
print()

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')

print()
print()

print(f'Перечень экспертов:\n\n{reviewer_1}\n\n{reviewer_2}')

print()
print()

students = [student_1, student_2, student_3]
lecturers = [lecturer_1, lecturer_3]


def av_rate_course_stu(course, students):
    sum = 0
    count = 0
    for student in students:
        sum_rate = student.av_rating_course(course)
        sum += sum_rate
        count += 1
    result = round(sum / count, 2)
    return result


def av_rate_course_lec(course, lecturers):
    sum = 0
    count = 0
    for lecturer in lecturers:
        lecturer_sum_rate = lecturer.av_rating_course(course)
        sum += lecturer_sum_rate
        count += 1
    result = round(sum / count, 2)
    return result


print('Подсчет средней оценки за домашние задания студентов курса Git')
print(av_rate_course_stu('Git', students))

print('Подсчет средней оценки за лекции лекторов курса Python')
print(av_rate_course_lec('Python', lecturers))
