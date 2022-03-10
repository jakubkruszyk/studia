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
        t_num = input("Podaj liczbę nauczycieli: ")
        for i in range(int(t_num)):
            self.teachers.append(Teacher())

        c_num = input("Podaj liczbę kursów: ")
        for i in range(int(c_num)):
            self.courses.append(Course(self.teachers))

        s_num = input("Podaj liczbę studentów: ")
        for i in range(int(s_num)):
            self.students.append(Student(self.courses))

    def __repr__(self):
        return f"{self.name} school. Address: {self.address}"


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
        self.semester = input("Podaj semestr: ")
        self.students = []
        pesel = input("Podaj pesel nauczyciela: ")
        for teacher in teachers:
            if teacher.pesel == pesel:
                teacher.courses.append(self)
                self.teacher = teacher

    def __repr__(self):
        return f"{self.name}, semester: {self.semester}, teacher: {self.teacher}"


class Student:
    def __init__(self, courses):
        self.pesel = input("Podaj pesel: ")
        self.email = input("Podaj email: ")
        self.semester = input("Podaj semestr: ")
        self.courses = []
        num = input("Podaj liczbę kursów: ")
        if int(num) > len(courses):
            num = len(courses)
        for i in range(int(num)):
            name = input("Podaj nazwę kursu: ")
            course = [c for c in courses if c.name == name]
            if course:
                self.courses.append(course[0])
                course[0].students.append(self)
            else:
                print("Zła nazwa kursu")

    def __repr__(self):
        return f"Email: {self.email}, semester: {self.semester}"


nowa = School()
