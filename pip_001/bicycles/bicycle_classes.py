class Component(object):

	"""Defines a generic bicycle component"""

	def __init__(self, name, itemid, weight, cost):
		self.name = name
		self.itemid = itemid
		self.weight = weight
		self.cost = cost
		

class Wheel(Component):

	"""Defines a bicycle wheel"""


class Frame(Component):

	"""Defines a bicycle frame"""

	def __init__(self, name, itemid, weight, cost, material = 'steel'):
		self.material = material
		super(Frame, self).__init__(name, itemid, weight, cost)


class Model(object):

	"""Defines a bicycle model"""

	def __init__(self, name, frame, wheel, manufacturer = ""):
		self.name = name
		self.frame = frame
		self.wheel = wheel
		self.manufacturer = manufacturer
		self.itemid = self.frame.itemid + '-' + self.wheel.itemid
		self.weight = (2 * self.wheel.weight) + self.frame.weight
		self.cost = (2 * self.wheel.cost) + self.frame.cost
		

class Business(object):

	"""Defines a generic business"""

	def __init__(self, name, markup):
		self.name = name
		self.markup = markup
		self.profit = 0

	def price(self, model):
		if model in self.inventory:
			return model.cost * (1 + self.markup)

	def catalog(self, models = [], personal = "\b"):
		if models == []:
			models = self.inventory
		if personal != "\b":
			personal = "just for " + personal
		print ""
		print "Here's what we've got for sale %s at %s:" % (personal, self.name)
		for model in models:
			print "%s: %s %s, total weight: %dg, price %.2f" % (model.itemid, model.manufacturer, model.name, model.weight, self.price(model))

	def buy(self, seller, model):
		if seller.sell(model):
			self.inventory.append(model)
			print ""
			print "%s just bought a %s %s for %.2f." % (self.name, model.manufacturer, model.name, model.cost)

	def sell(self, model):
		if model in self.inventory:
			price = self.price(model)
			margin = price - model.cost
			self.profit += margin
			model.cost = price
			self.inventory.remove(model)
			print ""
			print "%s just sold a %s %s for %.2f at a profit of %.2f." % (self.name, model.manufacturer, model.name, price, margin)
			return True
		else:
			print "That model is not available."
			return False

	def audit(self):
		self.catalog()
		print ""
		print "... and we have thus far made %.2f" % self.profit


class Manufacturer(Business):

	"""Defines a bicycle manufacturer"""

	def __init__(self, name, markup, inventory = []):
		self.inventory = []
		super(Manufacturer, self).__init__(name, markup)

	def make(self, model):
		model.manufacturer = self.name
		self.inventory.append(model)
		print ""
		print "%s just made a %s for %.2f." % (self.name, model.name, model.cost)


class Shop(Business):

	"""Defines a bicycle shop"""

	def __init__(self, name, markup = .2, inventory = []):
		self.inventory = []
		super(Shop, self).__init__(name, markup)


class Customer(object):

	"""Defines a bicycle customer"""

	def __init__(self, name, kitty, bicycle = None):
		self.name = name
		self.kitty = kitty
		self.bicycle = bicycle

	def browse(self, shop):
		afforable_models = [model for model in shop.inventory if shop.price(model) <= self.kitty]
		shop.catalog(afforable_models, self.name)

	def buy(self, shop, model):
		if shop.sell(model):
			self.kitty -= model.cost
			self.bicycle = model
		print ""
		print "%s is the proud new owner of a %s %s, which cost %.2f." % (self.name, self.bicycle.manufacturer, self.bicycle.name, self.bicycle.cost)
		print "%s now has %.2f left in the kitty." % (self.name, self.kitty)
