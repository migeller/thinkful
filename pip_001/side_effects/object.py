# Creating a user class
class User(object):
  def __init__(self, name):
    self.name = name
  def introduce(self):
    print "My name is", self.name

# Defining a function that will take a string and object and 
# modify them locally
def change(set, object):
  set = {'a', 'b'}
  object.name = "another new name"

# Creating our user and string
fred = User("fred")
bill = {'c', 'd'}

# Showing their current values
fred.introduce()
print bill
print type(fred)
print type(bill)

# Calling the function that makes changes to them locally
change(bill, fred)

# Showing their values after the change
fred.introduce()
print bill