from swimming import Shark, BlueWhale
from walking import Capybara, Elephant
from flying import Eagle, Swan
from habitats import PettingZoo, Aviary

bruce = Shark("Bruce", "Great White Shark", "Morning", "Seaweed")
emily = BlueWhale("Emily", "Blue whale", "Evening", "Krill")

joe = Capybara("Joe", "Fuzzy capybara", "Afternoon", "Pumpkin", 4, 6)
simon = Elephant("Simon", "Indian elephant", "Morning", "Leaves", 2)

joe.swim()
joe.walk()

tessa = Eagle("Tessa", "Golden eagle", "Evening", "House cat")
jaqueline = Swan("Jacqueline", "White swan", "Morning", "Tadpoles")

varmint_village = PettingZoo("Varmint Village")

varmint_village.animals.append(joe)
varmint_village.animals.append(simon)

flappy_town = Aviary("Flappy Town")
flappy_town.animals.append(tessa)
flappy_town.animals.append(jaqueline)



