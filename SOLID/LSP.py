# LSP - Liscov Substitution Principle


class Rectange:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = 10 * w
    print(f"Oczekiwana wartość pola: {expected_area}, rzeczywista {rc.area}")


rc = Rectange(2, 3)
use_it(rc)


# Łamiemy L
class Square(Rectange):
    def __init__(self, size):
        Rectange.__init__(self, size, size)

    @Rectange.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectange.height.setter
    def height(self, value):
        self._height = self._width = value


sq = Square(5)
use_it(sq)