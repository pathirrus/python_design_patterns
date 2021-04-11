# OCP - Open-Close Principle
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]


# Łamiemy O
class ProductFilter:
    # state-space explosion
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, products, color, size):
        for p in products:
            if p.size == size and p.color == color:
                yield p


pf = ProductFilter()
print(f"Green products:")
for p in pf.filter_by_color(products, Color.GREEN):
    print(f"  - {p.name} is green")

print(f"Large products:")
for p in pf.filter_by_size(products, Size.LARGE):
    print(f"  - {p.name} is large")

print(f"Large and blue products:")
for p in pf.filter_by_color_and_size(products, Color.BLUE, Size.LARGE):
    print(f"  - {p.name} is large and blue")


# W zgodzie z OCP
# Wykorzystujemy wzorzec specyfikacji (Enterprise patterns)
class ISpecification:
    def is_satisfied(self, item):
        pass


class ColorSpecification(ISpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class BetterFilter:
    def filter(self, items, specifiaction: ISpecification):
        for item in items:
            if specifiaction.is_satisfied(item):
                yield item


bf = BetterFilter()
green = ColorSpecification(Color.GREEN)
print("Green products (new way):")
for p in bf.filter(products, green):
    print(f"  - {p.name} is green")


class SizeSpecification(ISpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


print("Large products (new way):")
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f"  - {p.name} is large")


# A co z state-space explosion ?
# Kombinator (combinator)
class AndSpecification(ISpecification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


large_blue = AndSpecification(
    SizeSpecification(Size.LARGE),
    ColorSpecification(Color.BLUE)
)


print("Large, blue items (new_way):")
for p in bf.filter(products, large_blue):
    print(f"  - {p.name} is large and blue")