from swimming import Shark, BlueWhale
from walking import Capybara, Elephant
from flying import Eagle, Swan
from habitats import PettingZoo, Aviary

bruce = Shark("Bruce", "Great White Shark")
emily = BlueWhale("Emily", "Blue whale")

joe = Capybara("Joe", "Fuzzy capybara")
simon = Elephant("Simon", "Indian elephant")

tessa = Eagle("Tessa", "Golden eagle")
jaqueline = Swan("Jacqueline", "White swan")

varmint_village = PettingZoo("Varmint Village")

varmint_village.animals.append(joe)
varmint_village.animals.append(simon)

print(varmint_village.animals)

flappy_town = Aviary("Flappy Town")
flappy_town.animals.append(tessa)
flappy_town.animals.append(jaqueline)

print( f"{flappy_town.attraction_name} is where you will find {flappy_town.description}, like")
for animal in flappy_town.animals:
    print(f"{animal.name} the {animal.species}")
