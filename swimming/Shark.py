from datetime import date
from animal import Animal

class Shark(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True
