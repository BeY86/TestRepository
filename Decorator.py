def Decorator(func):
    def wrapper():
        print("Код до")
        func()
        print("Код после")

    return wrapper


@Decorator
def show():
    print("Код функции!")


show()
