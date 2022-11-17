#OOPs is Object Oriented Programming

class Person ():
  pass

# In order to avoid the IDE from stating that there is nothing inside the class, we use "pass" keyword.

# Now to create an object of class "Person"

person1 = Person()

# Now to assign some attributes to class

person1.age = 24
person1.name = "Arunima"
person1.favourite_color = "none"

print(person1.age)
print(person1.name)

# Creating a "method" that will be common to all the objects.

# Instance is an object that belongs to a class. For example, "list" is a class and if we create a list, we have an instance of "list" class.

# "Self" refers to the current instance of the class and is used to access variables that belongs to the class.

class Man():
  def print_name(self):
    print("Arunima Shukla")
  
person = Man()
person.print_name()
