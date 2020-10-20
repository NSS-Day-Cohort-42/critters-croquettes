import swimming
from animal.swimming import Swimming
from datetime import date
from animal import Animal
from animal import Swimming
from animal import Walking

class Capybara(Animal, Swimming, Walking):

    def __init__(self, name, species, shift, food, swimming_speed, walking_speed):
        Animal.__init__(self, name, species, shift, food)
        Swimming.__init__(self, swimming_speed)
        Walking.__init__(self, walking_speed)
