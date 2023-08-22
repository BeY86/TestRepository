class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 2


igor = Student()
igor.set("Игорь", 20)
print(igor.name, igor.age)

vlad = Person()
vlad.set("Влад", 25)
print(vlad.name, vlad.age)
