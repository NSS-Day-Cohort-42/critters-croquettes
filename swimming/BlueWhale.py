import swimming
from animal.swimming import Swimming
from datetime import date
from animal import Animal
from animal import Swimming

class BlueWhale(Animal, Swimming):

    def __init__(self, name, species, shift, food, swimming_speed):
        Animal.__init__(self, name, species, shift, food)
        Swimming.__init__(self, swimming_speed)

