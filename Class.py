class Person:
    name = "Ivan"
    age = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 2

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


igor = Student(
    "Игорь",
    22,
)
igor.set("Вася", 19, 4)
# igor.set("Игорь", 20)
print(igor.name, igor.age, igor.course)

vlad = Person("Влад", 14)
# vlad.set("Влад", 25)
print(vlad.name, vlad.age)
