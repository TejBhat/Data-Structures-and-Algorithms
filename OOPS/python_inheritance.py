#Create a class named Student, which will inherit the properties and methods from the Person class:
"""
class Student(Person):
  pass
  
"""
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

class A:
  def feature1(self):
    print("feature one is working")
  def feature2(self):
    print("feature two is working")

class B(A):#here we are inheriting the feature of parent class A
  def feature3(self):
    print("feature three is working")
  def feature4(self):
    print("feature four is working")
    
class C(A,B):
  def feature5(self):
    print("feature five is working")
  
  

a1=A()
a1.feature1
a1.feature2
b1=B()


#here A is super class and B is subclass

#singlelevel inheritance A->B
#multilevel inheritance A->B->C
#multiple inheritance c->A and B