# Loose coupling (luźne powiązania/sprzężenia)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Cześć, nazywam się {self.name}")


class Main:
    def __init__(self):
        user = User("Mark", 30)
        user.say_hello()


Main()