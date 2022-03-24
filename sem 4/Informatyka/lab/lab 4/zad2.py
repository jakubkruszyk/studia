class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def hello(self):
        print("Hello")


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def hello(self):
        print("test")


x = Square(1)
x.hello()
