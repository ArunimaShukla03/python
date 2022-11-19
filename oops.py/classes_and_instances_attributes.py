# Attributes whose values change from one instance to another is called instance attribute.

# Creating attributes like name, price or quantity could be good examples to put some information, we will do so in a constructor.

class Item():
  after_discount = 0.8
  
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    
  def apply_discount(self):
    return self.price * Item.after_discount
    

item1 = Item(name="shirt",price=10, quantity=50)
item2 = Item(name="pens",price=2, quantity=100)

# Now we want to apply 20% discount to all the items in the store. It will be not efficient to go and reduce price of each item therefore we use something called "class attributes".

# Class attributes will be global and accessible from each of our instance. This will be created from the very first line after you create a class.

print(f"The price of {item1.name} after discount is {item1.apply_discount()}")

# Class attributes are accessible from the object itself too.

print(item1.after_discount)

# First the attributes are searched inside a instance itself and if it is not found in it then it is searched in the class. Therefore if we define it in the instance itself it will give that value as an output instead of the attribute value in the class. For example:

item2.after_discount = 0.7

print(item2.after_discount)

# While class attribute is shared by all instance, an instance attribute is unique to that instance.