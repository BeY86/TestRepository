def Decorator(func):
    def wrapper():
        print("Start Programm!")
        func()
        print("Stop Programm!")

    return wrapper


@Decorator
def show():
    print("Hello World!")


show()
