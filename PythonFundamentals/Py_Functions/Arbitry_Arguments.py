##In this we will learn about arbitry(*args) and keyword arbitry arguments(**kwargs)

#In *args we are not sure how many arguments will come to the function

def calculator(*numbers):
    print(numbers)
    print(type(numbers))
num=calculator(1,2,3,4,5)

def addition(*numbers):
    add=0
    for x in numbers:
     add=add+x;
    return add;

sendNumbers=addition(1,2,3,4,5,6,7,8,9)
print(sendNumbers)  
sendNumbers1=addition(10,20,30)
print(sendNumbers1)  

# Using *args with Regular Arguments

def my_function(greeting,*names):
   for name in names:
      print(greeting,name,"!")
my_function("Hello","Bibhu","RIcha","Jayant","Niti") 

print("\n---------Finding maximum value---------------\n")
def findingMaximumValue(*numbers):
   length=len(numbers);
   if length==0:
      return None;
   max=numbers[0]
   for x in numbers:
      if x > max:
         max=x;
   return max;
print(findingMaximumValue(3,2,1,4,7,5))
print(findingMaximumValue(30,200,1,41,7,50))

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name
print("\n----------*kwargs-------------\n")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Using **kwargs with Regular Arguments
print("\n----------Using **kwargs with Regular Arguments--------------\n")
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs
print("\n---------Combining *args and **kwargs------------\n")
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:
print("\n---------Unpacking Arguments------------\n")
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

# Unpacking Dictionaries with **
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

print("\n------------Unpacking Dictionaries with **---------\n")
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

print("\n------------Unpacking Dictionaries with ** example 2---------\n")

def my_fruitFunction(fruitName,fruitPrice):
   print("Hello",fruitName," and price is ",fruitPrice)

fruitDict={"fruitName":"Apple","fruitPrice":200}
my_fruitFunction(**fruitDict)
