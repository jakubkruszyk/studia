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
    def __init__(self, name, addr):
        self.name = name
        self.address = addr
        self.teachers = []
        self.courses = []
        self.students = []

    def __repr__(self):
        return f"{self.name} school. Address: {self.address}"


class Teacher:
    def __init__(self, pesel, email, st):
        self.pesel = pesel
        self.email = email
        self.st = st
        self.courses = []

    def __repr__(self):
        return f"St. {self.st}, email: {self.email}"


class Course:
    def __init__(self, name, semester, teacher):
        self.name = name
        self.semester = semester
        self.teacher = teacher
        self.students = []

    def __repr__(self):
        return f"{self.name}, semester: {self.semester}, teacher: {self.teacher}"


class Student:
    def __init__(self, pesel, email, semester):
        self.pesel = pesel
        self.email = email
        self.semester = semester
        self.courses = []

    def __repr__(self):
        return f"Email: {self.email}, semester: {self.semester}"

