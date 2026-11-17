##The Properties are varible which we initilize belongs to class.
#those varible used to store the information of objects created within class.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

##Access the properties using dot natation

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

###Modify the properties
class Employee:
  def __init__(self,name,age,location):
    self.name=name;
    self.age=age;
    self.location=location;

e1=Employee("Bibhu",10,"Bangalore")
print(e1.name)
print(e1.age)
print(e1.location)

e1.name="Jayant"
e1.age=20;
e1.location="Narkatiaganj"

print(e1.name)
print(e1.location)
print(e1.age)

#Delete the properties usinf "del":
del e1.age;
# print(e1.age)

#Class Properties vs Object properties:
#Properties declared within the method called Object properties and
#Properties declared outsode methods called "class properties"

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#Modifying class properties
#When we modify class properties it affetcs all objects

Person.species="Animal"

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Add New Properties
p1.color="Black"

print(p1.color)