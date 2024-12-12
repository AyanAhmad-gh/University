from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def show_details(self):
        pass
