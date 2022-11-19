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
    
  def read(self):
    print(f"I finished the book, it had {self.PageCount} pages.")
    
book1 = Book(name="five feet apart", PageCount=200)
book1.read()

book2 = Book("the bell jar", 600)
book2.read()
