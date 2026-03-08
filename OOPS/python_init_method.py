#The __init__() Method
#All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
#The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("tj",26)
print(p1.name)
print(p1.age)

#Note: The __init__() method is called automatically every time the class is being used to create a new object.

#Why Use __init__()?
#Without the __init__() method, you would need to set properties manually for each object:

class Person:
    pass
p1=Person()
p1.name="tjj"
p1.age=26
print(p1.name)
print(p1.age)

#---------------------------------------------------------------------------------------------

#The self Parameter
#The self parameter is a reference to the current instance of the class.
#It is used to access properties and methods that belong to the class.
    
#Use self to access class properties:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

#Note: The self parameter must be the first parameter of any method in the class.

#self Does Not Have to Be Named "self"
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:
#Use the words myobject and abc instead of self:

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

#--------------------------------------------------------------------------
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()#same like Calculator clac=new Calculator() in java
print(calc.add(5, 3))
print(calc.multiply(4, 7))