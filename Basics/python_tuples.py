#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable amd allow duplicates

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#tuple constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#("apple", "kiwi", "cherry")

#Add Items
#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

#1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
#Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.


#Remove Items
#Note: You cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#Or you can delete the tuple completely:

#Example
#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#-------------------------------------------------------------------------------------------
"""
Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
1.count()-->Returns the number of times a specified value occurs in a tuple
2.index()-->Searches the tuple for a specified value and returns the position of where it was found
"""