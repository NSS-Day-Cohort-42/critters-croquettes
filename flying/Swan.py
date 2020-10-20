from datetime import date
from animal import Animal

class Swan(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.flying = True
        self.swimming = True

