# Lists are used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values(mutable)
#List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# output:3

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#['apple', 'banana', 'cherry']

#Change Item Value
#To change the value of a specific item, refer to the index number:

#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Note:
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#ADD IN LISTS
#Append Items
#To add an item to the end of the list, use the append() method:
#Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Insert Items
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#Note: As a result of the examples above, the lists will now contain 4 items.

#Extend List
#To append elements from another list to the current list, use the extend() method.

#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#The elements will be added to the end of the list.

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#----------------------------------------------------------------------------------------------------------

#Remove Specified Item
#The remove() method removes the specified item.

#Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#If there are more than one item with the specified value, the remove() method removes the first occurrence:

#Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.

#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.

#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely.

#Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.
#Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#-------------------------------------------------------------------------------
"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
1.append()	Adds an element at the end of the list
2.clear()	Removes all the elements from the list
3.copy()	Returns a copy of the list
4.count()	Returns the number of elements with the specified value
5.extend()	Add the elements of a list (or any iterable), to the end of the current list
6.index()	Returns the index of the first element with the specified value
7.insert()	Adds an element at the specified position
8.pop()	Removes the element at the specified position
9.remove()	Removes the item with the specified value
10.reverse()	Reverses the order of the list
11.sort()	Sorts the list
"""
