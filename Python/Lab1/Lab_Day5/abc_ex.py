#Th Abstract Base clss

import abc
help(abc)

from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self,reproductioncount):
        self.reproductioncount = reproductioncount
    @abstractmethod          #decorators
    def eat(self):
        pass

    def communicate(self):
        return "tweet"

class Finch(Bird):
    def eat(self,worms):
        return "yum"

freddyfichoff = Finch(1)
print(freddyfichoff.communicate())
print(freddyfichoff.eat(14))

class Penguin(Bird):
    def ear(self,fish):
        return"yum fish"

print()