from random import randint
import math

dct = {"x": 1, "y": 2, "z": 3}
# wprowadzone dicty, iteracje, dostęp do elementów


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point  x: {self.x}, y: {self.y}, z: {self.z}"


def distance(obj: Point):
    return math.sqrt(obj.x ** 2 + obj.y ** 2 + obj.z ** 2)


new_list = [Point(randint(0, 20), randint(0, 20), randint(0, 20)) for _ in range(10)]
sorted_list = sorted(new_list, key=lambda obj: obj.x)
sorted_distance = sorted(new_list, key=distance)

for old, new in zip(new_list, sorted_list):
    print(f"old: {old}  new: {new}")

for old, new in zip(new_list, sorted_distance):
    print(f"old: {distance(old)}  new: {distance(new)}")
