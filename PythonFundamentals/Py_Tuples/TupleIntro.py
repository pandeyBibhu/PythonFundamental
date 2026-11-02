##Tuples are used to store the multiple items in a single varible
#Tuple is one of 4 built in data types in python used to store the collection of data.
#other three are List,Set and Dictonary.All with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable
#Tuples are written with round bracket.


##Create a tuple

thisTuple=("Bibhu","Richa","Jayant","Niti","Akhileshwar","Sandhya","Dakshit","Nishchay","Shreedha")
print(thisTuple)

##Tuples can be created without using brackets also.

myTuple="apple","banana","mango"
print(myTuple)

##Tuple Items
#Tuple items are ordered,Unchangeble and allow duplicate values
#Tuples items are indexed and the first item indexed would be index[0] and second index[1] etc
#

##Ordered
#When we say items are ordered and while inserting the Items into tupple it maintain insertion order.

##Unchangable
#When we created tuple once then we cannot make any type of changes like adding,removing,and Updating .

##Allow duplicates
#Like list its also allow duplicate value to be inserted.

tuples=("apple","mango","banana","grapes","apple","banana","mango")
print(tuples)

##Tuple Length
#To determine how many items tuple have use len()

length=len(tuples);
print(length)

##Create tuple with one item
#When we crate tuple with one item,we need to insert comma after item otherwise it will not reconise as a tuple
print("\n--------------Createing tuplease with one item with comma---------------\n")
oneItem=("Apple",)
print(type(oneItem))

print("\n--------------Createing tuplease with one item without comma---------------\n")
oneItem1=("Apple")
print(type(oneItem1))

##EMPTY tuple
print("\n----------Empty tuple-----------\n")
emptyTuple=();
print(type(emptyTuple))

##Tuple items and Data types:
#Tuple item can be of any data type
print("\n-------------Data type of Tuple-------------------\n")
stringTuple1=("Apple","banana","mango")
intTuple1=(10,2,3,20,5)
boolTuple=(True,False,False)

print(type(stringTuple1))
print(type(intTuple1))
print(type(boolTuple))

##The tuple constructor
#We can create tuple using Tuple constructor also
print("\n----------Creating tuple using constructor-----------------\n")
consTuple=tuple(("Bibhu","Richa","Jayant","Niti"))
print(consTuple)






