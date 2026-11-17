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
print("\n------Child class Inheriting the properties from parent class------------\n")
class Student(Person):
    pass;
s1=Student("Richa","Kumari")
s1.display()