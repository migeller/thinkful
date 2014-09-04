class Fish(object):
	breathes_in_water = True
	skin = "scales"
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def feed(self, amount):
		print self.name + " got fed %s!" % amount

class Goldfish(Fish):
	def move(self, speed):
		return self.name + " is swimming upright %s!" % speed

class Flounder(Fish):
	def move(self, speed):
		return self.name + " is swimming sideways %s!" % speed

class Aquarium(object):
	fish = []
	def __init__(self, fish):
		self.fish = fish
	def feed(self, amount):
		for fish in self.fish:
			fish.feed(amount)

assortment = [Goldfish("Spencer", "Gold"), Flounder("Melissa", "Greyish Brown"), Goldfish("Fred", "Platinum")]

my_aquarium = Aquarium(assortment)

for fish in my_aquarium.fish:
	print fish.name, fish.color

for fish in my_aquarium.fish:
	print fish.move('slowly')

my_aquarium.feed('a lot')
