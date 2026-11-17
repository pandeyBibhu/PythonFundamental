###SCOPE:
#A varible is only available from inside the region it is created.This is called scope.
###LOCAL SCOPE:
#A varible which is created inside a function belongs to the local scope of that function.and This can only be used inside that function

def my_func():
    x=300
    print(x)

my_func();

####Function Inside Function
#A local varible can be accessed from a function within the function

def my_function2():
    x=400;
    def childFunction():
        print(x)
    childFunction();

my_function2();

###GLOBAL scope:
#A varible creatd outside the function is global and can be used anyone.
y=500;
def myFunc():
    print(y)
myFunc();
print(y)    

##Naming Varible:
#If you declare a varible inside the function and same varible name is used outside the function as global scope.
#In this case,varible value inside the function will be accessible withon the function only.
#And Outside varible value will be access across function.

print("\n-----------Same varible name inside and Outside function name---------\n")
price=200

def my_function3():
    price=100;
    print("price inside the function is ",price)
my_function3();
print("price outside function ",price)

#Global Keyword:
##To make local varible to be used as global varible we can use GLOBAL keyword following varible name.
print("\n-------Using global keyword-------------\n")
def my_function4():
    global price;
    price=3000;
    print("Price is ",price)
my_function4();  

print("Price of outside the function ",price)

print("\n-------Using global keyword2------------\n")
print("\n--------Changing the value of globally declared varible outside the function----------\n")
myPrice=2000

def my_function5():
    global myPrice;
    myPrice=4000
    print("price inside the function is ",myPrice)
my_function5()
print("price outside the function is ",myPrice)

###Nonlocal keyword:
#Suppose we have created a varible inside a function is called local varible
#Now we have nested function and we usae same varible inside the child function
#following nonlocal keyword,then it will become usable for ouside function as well.
print("\n---------Using nonlocal keyword----------\n")
def my_function6():
    myPrice=100;
    print("Outside nested function price is ",myPrice)
    def childFunction():
        nonlocal myPrice;
        myPrice=200
        print("Inside child function myPrice is ",myPrice)
    childFunction();
    return myPrice;
print(my_function6())

####LEGB rule:
#L:Local-Inside the current function
#E:Enclosing-Inside the enclosing function(from inner to outer)
#G:Global-At top level of module
#B:Built in-In python built namespace

print("\n-------LEGB rule------------\n")
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
              