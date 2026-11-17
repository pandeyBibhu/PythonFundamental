###Decorator let you add extra behaviour to a function,Without changing the function code.
#A decorator takes another functin as input ,return new new function
#Basic decorator 
#We need to define the decorator first,Then we need to apply @decorator_name above to the function

print("\n-----------Decorator-----------\n")
def changecase(func):
             def myinner():
                     return func().upper()
             return myinner

@changecase
def myFunction():
        return "Hello Bibhu"
print(myFunction())

###Multiple decorator call
def changecases(func):
        def myinner():
                return func().upper();
        return myinner

@changecases
def myFunction1():
        return "hello Bibhu";

@changecases
def myFunction2():
        return "my name is bibhu pandey"
print(myFunction1())
print(myFunction2())

####Argument into decorated function

print("\n-------Argument into decorated function---------\n")
def changecases(func):
        def myinner(x):
            return func(x).upper();
        return myinner;
@changecases
def myFunction3(varible1):
        return  "hello "+varible1;
print(myFunction3("bibhu kumar pandey"))

##*args and **kwArgs
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))
