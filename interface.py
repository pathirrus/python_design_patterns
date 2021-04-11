import abc


class IPilot(abc.ABC):
    @abc.abstractmethod
    def turn_on(self):
        pass

    @abc.abstractmethod
    def turn_off(self):
        pass


class Pilot(IPilot):
    def turn_on(self):
        print("Włącz")

    def turn_off(self):
        print("Wyłącz")


p = Pilot()
p.turn_on()
p.turn_off()