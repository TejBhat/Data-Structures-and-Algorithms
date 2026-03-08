# Variables are containers for storing data values.

x=4
y="Tej"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x=10
x="Tej"
print(x)
#output->"tej" 
#because of interpretation
#Python allows this because it is dynamically typed, meaning the type of a variable is determined at runtime and can change.

#-------------------------------------------------------------

#Casting
#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


#---------------------------------------------------------------

#type()
# You can get the data type of a variable with the type() function.
 
x=4
z='string'
print(type(x))
print(type(z))

#----------------------------------------------------------------

#String variables can be declared either by using single or double quotes

# Case-Sensitive
# Variable names are case-sensitive(age, Age and AGE are three different variables).

#-----------------------------------------------------------------

#Camel Case
#Each word, except the first, starts with a capital letter:
#myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
#MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
#my_variable_name = "John"

#------------------------------------------------------------------

#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#--------------------------------------------------------------------

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

x = 5
y = "John"
print(x, y)
#output: 5 John

#error
x = 5
y = "John"
print(x + y)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'