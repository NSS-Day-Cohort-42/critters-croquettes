from datetime import date
from animal import Animal

class Eagle(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.flying = True
        self.walking = True
