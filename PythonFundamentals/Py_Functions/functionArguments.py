###Arguments and Parameters
##we can pass the ariguments in the function parantheses.for those arguments we can pass the value and those values can 
#be utilize inside that function.

def myFunction(name1):   #parameters got paased under function name within the paranthesis
    print("name is ",name1);

myFunction("Bibhu")#arguments passed to the functions
myFunction("Richa")#arguments passed to the functions
myFunction("Niti")#arguments passed to the functions
myFunction("jayant")#arguments passed to the functions
myFunction("Akhileshwar")#arguments passed to the functions
myFunction("Sandhya")#arguments passed to the functions

# Number of Arguments:
#By default a function can be called with excat number of arguments matches with parameter


# Default Parameter Values
#default parameter value can be assigned to parameters
#if a functions i called without an parameter then it uses default value like below:

def myfunction(name="Chandan"):
    print(name);
myfunction();#Called without any arguments
myfunction("Kyuji kaise ho");#called with arguments

# Keyword Arguments

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.

# Positional arguments must be in the correct order:
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

print("\n-----------Switching the order changes the result:----------------------\n")
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

# Mixing Positional and Keyword Arguments
#While mixing positional and keyword argurment ,position argument should come first in order and then keyword argument
print("\n------------mixing positional and keyword argument----------------\n")
def myNameFunction(name,age,location):
   print("My name is",name," and my age is",age," and I am from ",location)

myNameFunction("Bibhu",age=25,location="Bangalore")   

# Passing Different Data Types
#Wde can send any type of data type as an argument to a function(string,number,list,tuple,dictonaries)
#The data will be preserved in the function
print("\n-------Passing String datatype-------------\n")
def my_namefunction(name,location):
   print("My name is ",name," and My location is ",location)
my_namefunction("Bibhu","Bangalore");

print("\n------Passing number data type-----------------\n")
def myNumberType(num):
   print("the given number is ",num)
myNumberType(100)

print("\n---------Sending list data type----------------\n")
def listType(list):
   for x in list:
      print(x)
myNamesList=["Bibhu","richa","Jayant","Niti"];     
print(listType(myNamesList))

print("\n----------------Sending tuple data type-----------------\n")
def myFruits_tuple(tuplee):
   for x in tuplee:
      print(x)

fruitTuple=("Apple","Mango","Pineapple","Cherry")
print(myFruits_tuple(fruitTuple))

print("\n------------Sending dictonary data type----------------\n")
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

##return value

def my_return(x,y):
   return x+y;

print(my_return(10,20))

#Returning different data types
#Functions can return any data types like lis,tuple,dictonaries

print("\n----------Returning List data type------------------\n")
def returnListType():
   return ["Apple","Banana","Mango","cherry"]
print(returnListType())

print("\n-------------returning tuple data type-----------------\n")
def returningTuple():
   return ("Bibhu","Richa","Jayant","Richa")
print(returningTuple())

print("\n---------returning dictonaries data type----------------\n")
def returnDictonaries():
   return {"name":"Bibhu","age":20,"location":"Bangalore"}


print(returnDictonaries())