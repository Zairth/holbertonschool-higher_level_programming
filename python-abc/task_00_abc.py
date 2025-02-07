#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class inherited from ABC"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class inherited from Animal"""

    def sound(self):
        """Abstract method that implemente the parent method"""

        return "Bark"


class Cat(Animal):
    """Class inherited from Animal"""

    def sound(self):
        """Abstract method that implemente the parent method"""

        return "Meow"
