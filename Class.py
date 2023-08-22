# class Person:
#    name = "Ivan"
#    age = 10
#
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def set(self, name, age):
#        self.name = name
#        self.age = age
#
#
# class Student(Person):
#    course = 2
#
#    def set(self, name, age, course):
#        self.name = name
#        self.age = age
#        self.course = course
#
#
# igor = Student(
#    "Игорь",
#    22,
# )
# igor.set("Вася", 19, 4)
## igor.set("Игорь", 20)
# print(igor.name, igor.age, igor.course)
#
# vlad = Person("Влад", 14)
## vlad.set("Влад", 25)
# print(vlad.name, vlad.age)


class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance  # Используйте self для инициализации атрибута

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount} единиц. Текущий баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной!")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Снято {amount} единиц.Текущий баланс {self.balance}")

    def get_balande(self):
        print(f"У вас на счету {self.balance}")


account = BankAccount("12345", "John Doe")
account.deposit(100)
account.withdraw(25)
account.get_balande()
