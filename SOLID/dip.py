# DIP - Dependency Inversion Principle

# Łamiemy D
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

# print(relationships.relations)


# W zgodzie z D
class Research:
    # Szukamy wszystkich dzieci
    def __init__(self, relationships):
        for r in relationships.relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John ma dziecko o imieniu {r[2].name}")


# Research(relationships)

import abc


class IRelationshipsBrowser(abc.ABC):
    @abc.abstractmethod
    def find_all_children_of(self, person_name):
        pass


class RelationshipsBrowser(IRelationshipsBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, person_name):
        for r in relationships.relations:
            if r[0].name == person_name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser: IRelationshipsBrowser):
        for p in browser.find_all_children_of("John"):
            print(f"John ma dziecko o imieniu {p}")


relationships = RelationshipsBrowser()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)