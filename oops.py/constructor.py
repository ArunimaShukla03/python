# The __init__ function runs as soon as the instance of a class is created.

class Creation():
  def __init__(self):
    print("OH IM CREATED")
    
create1 = Creation()

class Employee():
  def __init__(self, name, role):
    self.name = name
    self.role = role
    
employee1 = Employee(name='arunima', role='developer')
print(employee1.name)

class Book():
  def __init__(self, name, PageCount):
    self.name = name
    self.PageCount = PageCount
    
read = Book(name = "five feet apart", PageCount="350")

print("I finished the book, it had", read.PageCount , "pages.")

