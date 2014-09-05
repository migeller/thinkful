from bicycle_classes import Wheel, Frame, Model, Manufacturer, Shop, Customer

# Frames
eliminator = Frame("Eliminator", "EX-12", 120, 400, "carbon")
gazelle = Frame("Gazelle", "GX-7", 180, 200, "aluminium")
beater = Frame("Beater", "B-1", 250, 100)

# Wheels
whisper = Wheel("Whisper", "W1200Z", 50, 80)
outback = Wheel("Outback", "O750X", 75, 35)
rotund = Wheel("Rotund", "R100A", 100, 15)

# Models
elite = Model("Elite", eliminator, whisper)
rugged = Model("Rugged", gazelle, outback)
get_around = Model("Get Around", beater, rotund)

super_fine = Model("Super Fine", eliminator, whisper)
just_fine = Model("Just Fine", gazelle, outback)
not_so_fine = Model("Not So Fine", beater, rotund)

# Manufacturers
reliant = Manufacturer("Reliant", .15)
forward_motion = Manufacturer("Forward Motion", .25)

# Shop
mels_bikes = Shop("Mel's Bikes", .2)

# Customer
matt = Customer("Matt", 1000)
drew = Customer("Drew", 500)
lisa = Customer("Lisa", 200)

# Make Reliant Models
r_work_order = [elite, rugged, get_around]

for model in r_work_order:
	reliant.make(model)

reliant.catalog()

# Make Forward Motion Models
fm_work_order = [super_fine, just_fine, not_so_fine]

for model in fm_work_order:
	forward_motion.make(model)

forward_motion.catalog()

# Buy Bikes for Mel's Bikes
purchase_order = [(reliant, elite), (reliant, rugged), (reliant, get_around), (forward_motion, super_fine), (forward_motion, just_fine), (forward_motion, not_so_fine)]

for order in purchase_order:
	mels_bikes.buy(order[0], order[1])

# Conduct Audit of Mel's Bikes
mels_bikes.audit()

# Customers Browse Mel's Bikes
matt.browse(mels_bikes)

drew.browse(mels_bikes)

lisa.browse(mels_bikes)

# Customers make purchases
matt.buy(mels_bikes, elite)

drew.buy(mels_bikes, rugged)

lisa.buy(mels_bikes, not_so_fine)

# Final Audit of Mel's Bikes
mels_bikes.audit()

# Make sure markups are right
print mels_bikes.markup
print reliant.markup
print forward_motion.markup
