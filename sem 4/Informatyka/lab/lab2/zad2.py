from datetime import datetime

# Klasa szkoła
# konstruktor - Nazwa, adres,
# listy - nauczyciele, kursy, studenci

# Klasa nauczyciel
# pesel, email, stopien, kursy[]

# Klasa kurs
# nazwa, semestr, studenci[], nauczyciel

# Klasa student
# pesel, email, semestr, kursy[]


class School:
    def __init__(self):
        self.name = input("Podaj nazwę: ")
        self.address = input("Podaj adres: ")
        self.teachers = []
        self.courses = []
        self.students = []
        num = input("Podaj liczbę nauczycieli: ")
        num = int(num) if num.isnumeric() else 0
        for i in range(num):
            self.add_teacher()

        num = input("Podaj liczbę kursów: ")
        num = int(num) if num.isnumeric() else 0
        for i in range(num):
            self.add_course()

        num = input("Podaj liczbę studentów: ")
        num = int(num) if num.isnumeric() else 0
        for i in range(num):
            self.add_student()

    def __repr__(self):
        return f"{self.name} school. Address: {self.address}"

    def print_students(self):
        students_sorted = sorted(self.students, key=lambda s: s.email)
        for student in students_sorted:
            print(student)
    
    def print_teachers(self):
        teachers_sorted = sorted(self.teachers, key=lambda t: t.email)
        for teacher in teachers_sorted:
            print(teacher)

    def print_courses(self, sem):
        courses_filtered = [c for c in self.courses if c.semester == sem]
        if courses_filtered:
            for course in courses_filtered:
                print(course)
        else:
            print("Nie znaleziono kursów dla danego semestru")

    def print_students_age(self):
        students_sorted = sorted(self.students, key=lambda s: s.birth_date().timestamp(), reverse=True)
        for student in students_sorted:
            print(student)

    def add_student(self):
        self.students.append(Student(self.courses))

    def add_course(self):
        self.courses.append(Course(self.teachers))

    def add_teacher(self):
        self.teachers.append(Teacher())

    def average(self):
        average_list = {c.name: [] for c in self.courses}
        students_results = [student.average() for student in self.students]
        for result in students_results:
            for course in result:
                average_list[course].append(result[course])

        for course in average_list:
            if average_list[course]:
                average_list[course] = sum(average_list[course])/len(average_list[course])
            else:
                average_list[course] = 0
        return average_list


class Teacher:
    def __init__(self):
        self.pesel = input("Podaj pesel: ")
        self.email = input("Podaj email: ")
        self.st = input("Podaj stopień: ")
        self.courses = []

    def __repr__(self):
        return f"St. {self.st}, email: {self.email}"


class Course:
    def __init__(self, teachers):
        self.name = input("Podaj nazwę: ")
        self.semester = int(input("Podaj semestr: "))
        self.students = []
        pesel = input("Podaj pesel nauczyciela: ")
        teacher = [t for t in teachers if t.pesel == pesel][0]
        if teacher:
            teacher.courses.append(self)
            self.teacher = teacher
        else:
            print("Nie znaleziono nauczyciela z danym numerem pesel")

    def __repr__(self):
        return f"{self.name}, semester: {self.semester}, teacher: {self.teacher}"


class Student:
    def __init__(self, courses):
        self.pesel = input("Podaj pesel: ")
        self.email = input("Podaj email: ")
        self.semester = input("Podaj semestr: ")
        self.courses = []
        self.grades = {}
        num = input("Podaj liczbę kursów: ")
        num = int(num) if num.isnumeric() else 0
        if num > len(courses):
            num = len(courses)
        for i in range(num):
            name = input("Podaj nazwę kursu: ")
            course = [c for c in courses if c.name == name][0]
            if course:
                self.courses.append(course)
                course.students.append(self)
                self.grades[course.name] = []
            else:
                print("Zła nazwa kursu")

    def __repr__(self):
        return f"Email: {self.email}, semester: {self.semester}"

    def add_grade(self, course, grade):
        grade_list = self.grades.get(course)
        if grade_list is None:
            print("Uczeń nie jest zapisany do tego kursu")
        else:
            grade_list.append(grade)

    def average(self, course=None):
        if course is None:
            average_list = {c: [] for c in self.grades}
        else:
            average_list = {course: []}
        for course in average_list:
            if self.grades[course]:
                average_list[course] = sum(self.grades[course])/len(self.grades[course])
            else:
                average_list[course] = 0
        return average_list

    def birth_date(self):  # 19xx 01 - 12   20xx 21 - 32    21xx 41 - 52
        year = int(self.pesel[0:2])
        month = int(self.pesel[2:4])
        day = int(self.pesel[4:6])
        if 0 < month < 13:
            year = 1900 + year
        elif 20 < month < 33:
            year = 2000 + year
            month = month - 20
        else:
            year = 2100 + year
            month = month - 40
        date = datetime(year, month, day)
        return date


nowa = School()
nowa.print_students()
nowa.print_teachers()
nowa.print_courses(1)
nowa.print_students_age()

nowa.students[0].add_grade("matematyka", 5.0)
nowa.students[0].add_grade("matematyka", 4.5)
nowa.students[0].add_grade("inf", 4.0)
nowa.students[0].add_grade("inf", 3.0)
print(nowa.students[0].average())
print(nowa.average())
nowa.print_students_age()
