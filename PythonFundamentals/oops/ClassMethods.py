##Methods are functions which belongs to class and they define the behaviour of objects created from class.
class welcome:
    
    def greet():
        print("Welcome to Python methods")

# w=welcome();
welcome.greet(); 

class Greet:
    def greet(self):#When we create instance method then "Self need to passwed as parameter for the first param"
        print("Welcome to the python world")

g=Greet();
g.greet();


##Methods with Parameters
class calculator:
    def add(self,a,b):
        print(a+b)
    def mul(self,a,b):
        print(a*b)
c=calculator();
c.add(10,20)
c.mul(10,20)   

##Methods which access properties
#Methods can access properties and modify methods using self
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def getInfo(self):
        return f"{self.name} is {self.age} year old"
p1=Person("Bibhu",20)

print(p1.getInfo())

##__str__():
#The __str__() method is a special method that controls what is returned when the object is printed.

class person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def __str__(self):
        return f"{self.name} {self.age}"
p1=person("Richa",30);
print(p1)    

##A class can have multiple methods
##A class methods can be deleted using del keyword