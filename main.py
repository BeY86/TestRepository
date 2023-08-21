class Percon:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age


Igor = Percon()
Igor.set("Igor", 19)
print(Igor.name, Igor.age)
