###Functions is block of code which could be used to whenever it is called.
##A function can return data as result
##using function we can avoid code repatation

##Creating function:
##A function is defined by "def" keyword followed by functionName and parantheses

def greeting():
    print("Welcome to functions module!!!")

##calling a function
greeting();
##We can call same function multiple times
greeting();
greeting();
greeting();

##function Name:
#Function name follow the same rules as varible in Python
#A function name must start with letter and Underscore
#A function name can only contain letters,numbers and underscores
#Functions name are case sensitive

##Return value:

def perform_Addition(a,b):
    return a+b;
add=perform_Addition(10,20)
print("Addition:::::",add);

###pass statement
#When we need to create the function without any code then we can use pass statement

def passStatement():
    pass;