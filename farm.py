class Animal:
    def __init__(self, name):
        self.name = name

    def spaek(self):
        pass


class Cow(Animal):
    def speak(self):
        print("Muuuuuu")


class Hen(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.egg_container = EggContainer(2)

    def speak(self):
        print("Ko ko ko ko")

    def get_egg(self):
        if not self.egg_container.amount:
            print("Nie mam już jajek")
        else:
            self.egg_container.decrease()
            print("Proszę jajko")


class EggContainer:
    def __init__(self, amount):
        self.amount = amount

    def decrease(self):
        self.amount -= 1

    def increase(self):
        self.amount += 1


if __name__ == "__main__":
    eva = Hen("Eva")

    print(eva.egg_container.amount)
    eva.get_egg()
    print(eva.egg_container.amount)
    eva.get_egg()
    print(eva.egg_container.amount)
    eva.get_egg()
    print(eva.egg_container.amount)