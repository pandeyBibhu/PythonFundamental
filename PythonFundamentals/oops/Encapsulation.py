###ENCAPSULATION:
#In thos oops principle we keep data.properties and Methode together and prvent access from outside of class.
#and It didnt expose the implementation of class outside or from another class.
#Which try to protect the external changes
#Private properties:

#we can make any properties a private by using double underscore(__) as prefix.
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.__age=age;

p1=Person("Bibhu",20)
print(p1.name);
# print(p1.__age);#this will throw error

#Private property cannot be access directly from outside of class.
#Accessing the Private properties.
#To access the private property we need to create the getter method.
print("\n----Accessing the private properties------\n")
class Employee:
    def __init__(self,name,age):
        self.name=name;
        self.__age=age;
    def get_age(self):
        return self.__age;
p1=Employee("Bibhu",23)
print(p1.name)
print(p1.get_age())

##SET the private property
#We can set the private property using setter method
print("\n---Using setter method to set the private property--------\n")
class Student:
    def __init__(self,name,age):
        self.name=name;
        self.__age=age;
    def get_age(self):
        return self.__age;
    
    def set_age(self,age):
        if age>0:
         self.__age=age;
        else:
            print("Valid positive age!")
s1=Student("Bibhu",28);
print("\n--Before setting---\n")
print(s1.name)
print(s1.get_age()) 
print("--After setting--\n")
s1.set_age(40);
print(s1.name)
print(s1.get_age())    

# Why Use Encapsulation?
# Encapsulation provides several benefits:

# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified

class Company:
    def __init__(self,name,age):
        self.name=name;
        self.__age=age;
    def set_age(self,age):
        if age<18:
            print("Not elegible to cast the vote!!")
        else:
            self.__age=age;
    def get_age(self):
        return self.__age;

c1=Company("Dell",40)
print("\n--Before setting---\n")

print("Company name: ",c1.name," age of the Company is: ",c1.get_age())

print("\n--After setting----\n")
c1.set_age(55);
print("Company name: ",c1.name," age of the Company is: ",c1.get_age())


###Protected properties:
#Create a protected properties
#We can create protected properties using single underscore(_) as prefix.
print("\n-----Protected properties-----\n")
class Animal:
    def __init__(self,name,age):
        self.name=name;
        self._age=age;#protected property

a1=Animal("Dog",2)
print(a1.name)
print(a1._age);


# Name Mangling
# Name mangling is how Python implements private properties and methods.

# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

# For example, __age becomes _Person__age.    
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!

# While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation.
