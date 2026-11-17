##Self parameter is  reference to the current instance of the classes.
#It is used to access the class properties and methods

class Car:
    def __init__(self,brand,color,price):
        self.brand=brand;
        self.color=color;
        self.price=price;

    def display(self):
        print("Brand of Car is ",self.brand," and color is ",self.color," price of car is ",self.price);

c1=Car("BMW","Black",2000)
c2=Car("Audi","Black",3000)
c3=Car("Lamborgini","Black",4000)

c1.display()
c2.display()
c3.display()

# Why Use self?
# Without self, Python would not know which object's properties you want to access:
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

# self Does Not Have to Be Named "self"
#it is not mandatory to be named as self,we can name it as anything we want but make sure that object is fisrtparameter of any method
class Employee:
   def __init__(myFav,ename,eAge,eDept):
      myFav.ename=ename;
      myFav.eAge=eAge;
      myFav.eDept=eDept;
   def printEmployee(fav):
     print("Name of Employeee is ",fav.ename," and his age is ",fav.eAge," and Depart of employee is ",fav.eDept,"\n");

e1=Employee("Bibhu",100,"Engineering");
e2=Employee("Jayant",200,"Management");

e1.printEmployee();
e2.printEmployee();