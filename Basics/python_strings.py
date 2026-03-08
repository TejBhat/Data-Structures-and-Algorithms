print("Hello")
print('Hello')
#here single and double quotation both are correct

#Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
#output: e
#------------------------------------------------------
#Looping Through a String
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)
#output
"""
b
a
n
a
n
a
"""
#--------------------------------------------------------
#String Length
#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))
#output:13--> also counts the spaces 

#--------------------------------------------------------
#Slicing

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
#output:llo

#Slice From the Start
#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])
#output:Hello

#Slice To the End
#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
#output:llo, World!

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:

#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])
#output:orl 
#negative indexing starts from -1
"""
| Character      | H   | e   | l   | l   | o  | ,  |    | W  | o      | r  | l      | d      | !  |
| -------------- | --- | --- | --- | --- | -- | -- | -- | -- | ------ | -- | ------ | ------ | -- |
| Negative Index | -13 | -12 | -11 | -10 | -9 | -8 | -7 | -6 | **-5** | -4 | **-3** | **-2** | -1 |
"""
#------------------------------------------------------------------------------
#Python has a set of built-in methods that you can use on strings.

#UPPER CASE
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#output:HELLO, WORLD!

#lowercase
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#output:hello, world!
#-------------------------------------------------------------------------------

#Remove Whitespace
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#--------------------------------------------------------------------------------
#Replace String
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!
#---------------------------------------------------------------------------------
#Split String
#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#----------------------------------------------------------------------------------

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)
#HelloWorld

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World

#-------------------------------------------------------------------------------------------------

#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
#But we can combine strings and numbers by using f-strings or the format() method!

#F-Strings
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)
#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
#Example
#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#output-The price is 59.00 dollars
#A placeholder can contain Python code, like math operations:
#Example
#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
