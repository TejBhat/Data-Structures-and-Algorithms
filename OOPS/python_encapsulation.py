#Encapsulation is about protecting data inside a class.
#It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
#This prevents accidental changes to your data and hides the internal details of how your class works.

#Private Properties
#In Python, you can make properties private by using a double underscore __ prefix:

#Create a private class property named __age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error
#Note: Private properties cannot be accessed directly from outside the class.

#Get Private Property Value
#To access a private property, you can create a getter method:

#Use a getter method to access a private property:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())

#Set Private Property Value
#To modify a private property, you can create a setter method.

#The setter method can also validate the value before setting it:

#Use a setter method to change a private property:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())