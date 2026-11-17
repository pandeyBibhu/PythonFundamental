##In pyhton magic methods are those who is written and followed by double underscore(__name__)

#__init__() && __str__():

class Employee:
    def __init__(self,name,age):  #the init method will be called automatically when objects is created
        self.name=name;
        self.age=age;
    def __str__(self): ##str methods will be invoked automatically for string representation of objects
        return f"{self.name} {self.age}"

e=Employee("Bibhu",20)
print(e)

##__repr__():
class Student:
    def __init__(self,name):
        self.name=name;
    def __repr__(self):
        return f"Student('{self.name})"
    def __str__(self):
        return f"{self.name}"
s=Student("Jayant")
print(s) 
print(repr(s))  

##__eq__():
print("\n------without__eq__()------\n")
class schools:
    def __init__(self,name):
        self.name=name;
    
s1=schools("Railway")
s2=schools("Railway")

print(s1==s2)
print("\n------with__eq__()------\n")
class school:
    def __init__(self,name):
        self.name=name;
    def __eq__(self,other):
        return self.name==other.name;

s1=school("Railway")
s2=school("Railway")

print(s1==s2)

##__add__():
##Using this method also called opertor overloading.
print("\n------__add__-------\n")
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def __add__(self,other):
        return self.age+other.age;
p1=Person("Bibhu",20);
p2=Person("Jayant",30);
print(p1+p2);

##__len__
print("\n--------without__len__----------\n")
# class Length:
#     def __init__(self,fruits):
#          self.fruits=fruits;
         
# l=Length(["Apple","Orange","Grapes","Watermelon"])
# print(len(l));

print("\n--------with__len__----------\n")
class Fruits:
    def __init__(self,fruits):
        self.fruits=fruits;

    def __len__(self):
     return len(self.fruits);     
f1=Fruits(["Apple","Orange","Grapes","Watermelon"])
print(len(f1));

##__it__()
#It is used to compare the objects

class Vegitables:
    def __init__(self,name,price):
        self.name=name;
        self.price=price;

    
    def __lt__(self,other):
      return self.price < other.price;

v1=Vegitables("Potato",20)
v2=Vegitables("Tomato",30)
print(v1 < v2);    

##Sorting with __lt__()
#The sorted() function returns a list with the given objects, sorted as specified in the __lt__() method.
print("\n----Sorting by __lt__-----------\n")
class Person:
   def __init__(self,name,age):
       self.name=name;
       self.age=age;
   def __lt__(self,other):
       return self.age < other.age;
p1=Person("Bibhu",40);
p2=Person("Jayant",20);
p3=Person("Akhileshwar",50)
p4=Person("Dakshit",7)
p5=Person("Nishchay",4)

x=sorted([p1,p2,p3,p4,p5]);
print(x[0].age) 

##__contains__:it control what the in operator checks for your own objects.

class Company:
    def __init__(self,employees):
        self.employees=employees;
    def __contains__(self, item):
      return item in self.employees;

c1=Company(["Bibhu","Richa","Niti","Sandhya"]);
print("Niti" in c1);
print("Niti1" in c1);