# ISP - Interface Segregation Principle
import abc


# Łamiemy I
class IMachine(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        pass

    @abc.abstractmethod
    def scan(self, document):
        pass

    @abc.abstractmethod
    def fax(self, document):
        pass


class MultiFunctionalPrinter(IMachine):
    def print(self, document):
        print("Drukuję")

    def scan(self, document):
        print("Skanuję")

    def fax(self, document):
        print("Wysyłam fax")

m = MultiFunctionalPrinter()
# m.print("dokument")


class OldFahionedPrinter(IMachine):
    def print(self, document):
        print("Drukuję")

    def scan(self, document):
        raise NotImplementedError("Nie umiem skanować")

    def fax(self, document):
        raise NotImplementedError("Nie umiem wysyłać faxu")


o = OldFahionedPrinter()
# o.scan("document")  # Ups!


# Nie łamiemy I
class IPrinter(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        pass


class IScan(abc.ABC):
    @abc.abstractmethod
    def scan(self, document):
        pass


class IFax(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        pass


class MyPrinter(IPrinter):
    def print(self, document):
        print("Drukuję")


m = MyPrinter()
# m.print("dokument")


class PhotoCopier(IPrinter, IScan):
    def print(self, document):
        print("Drukuję")

    def scan(self, document):
        print("Skanuję")


pc = PhotoCopier()
pc.scan("dokument")


class IMultiFunctionalMachine(IPrinter, IScan, IFax):
    pass