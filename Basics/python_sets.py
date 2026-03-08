#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed and duplicates not allowed.
#Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

#Add Items
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add Sets
#To add items from another set into the current set, use the update() method.
#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Add Any Iterable
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#Add elements of a list to a set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
#Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.

#Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.

#Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)



#Python frozenset
#frozenset is an immutable version of a set.
#Like sets, it contains unique, unordered, unchangeable elements.
#Unlike sets, elements cannot be added or removed from a frozenset.
#Creating a frozenset
#Use the frozenset() constructor to create a frozenset from any iterable.

#Create a frozenset and check its type:

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

"""
Frozenset Methods
Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

Method	Shortcut	Description	Try it
1.copy()	 	Returns a shallow copy	
2.difference()	-	Returns a new frozenset with the difference	
3.intersection()	&	Returns a new frozenset with the intersection	
4.isdisjoint()	 	Returns whether two frozensets have an intersection	
5.issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
6.issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
7.symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
8.union()	|	Returns a new frozenset containing the union
"""


"""
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Shortcut	Description
1.add()	 	Adds an element to the set
2.clear()	 	Removes all the elements from the set
3.copy()	 	Returns a copy of the set
4.difference()	-	Returns a set containing the difference between two or more sets
5.difference_update()	-=	Removes the items in this set that are also included in another, specified set
6.discard()	 	Remove the specified item
7.intersection()	&	Returns a set, that is the intersection of two other sets
8.intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
9.isdisjoint()	 	Returns whether two sets have a intersection or not
10.issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
11.issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
12.pop()	 	Removes an element from the set
13.remove()	 	Removes the specified element
14.symmetric_difference()	^	Returns a set with the symmetric differences of two sets
15.symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
16.union()	|	Return a set containing the union of sets
17.update()	|=	Update the set with the union of this set and others
"""