##Inheritence allow us inherit all the properties from parent class.
#Inheritence has child class and Parent class as term used in python.
#Child class is also know as derived class and Parent class is also called as Base class

#Create a Parent class

class Person:
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
    def display(self):
        print("FirstName: ",self.fname," lastName ",self.lname)
p1=Person("Bibhu","Pandey")
p2=Person("Jayant","Pandey")
p1.display();
p2.display()

##Create child class
#While creating the child class we need to pass parent class name as parameter in child class
#When we add init method inside child class ,then parent class init method will no loneger accessible
print("\n------Child class Inheriting the properties from parent class------------\n")
class Student(Person):
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
s1=Student("Richa","Kumari")
s1.display()

##To keep the accssible of parent init method we need to add call
class Parent:
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname;
    def display(self):
        print("FirstName:",self.fname," LastName:",self.lname)

# p1=Parent("Bibhu","Kumar")
# p1.display();

class child(Parent):
    def __init__(self, fname, lname):
        Person.__init__(self,fname, lname)
        # super().__init__(fname, lname)
c1=child("Richa","Mishra");
c1.display();
#####USE SUPER FUNCTION():
#Using super function we can inherit all the properties and Methods from Parent class.

print("\n-----Using super function--------\n")
class child2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
c2=child2("Jayant","Pandey")
c2.display();

####Adding the properties to child class
print("\n-----Adding properties to child class------\n")
class child3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.age=2019;
c3=child3("Dakshit","Pandey")
print(c3.age)

###Adding new parameter to child class
class child4(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.age=year;
c4=child4("Bibh","Kumar",2025)
c4.display()
print(c4.age)

###Adding a method into child class
print("\n-----Add method in child class-------\n")
class child5(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    def greet(self):
        print("welcome :",self.fname," ",self.lname)
c5=child5("Nisha","Kumari")
c5.greet();            