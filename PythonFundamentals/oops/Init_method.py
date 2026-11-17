##In python all classes have built menthod called _init_(),
#Its always get executed whenever the class is being initiated.
#The _init_() methode is used to assign  values to objects properties or operation are performed when the object is being created.

class employee:
    def __init__(self,name,department):
        self.name=name;
        self.department=department;

p1=employee("Bibhu","Engineering");
p2=employee("Jayant","Management");

print(p1.name," is from department ",p1.department);
print("\n")
print(p2.name," is from department ",p2.department);

##WHY we use __init__()
#If we dont use __init__() method then we may need to assign the values for each properties manually.
#creating class without __init__()

class person:
    pass;
p1=person();
p1.name="Bibhu";
p1.age=10;

print(p1.name)
print(p1.age)

###Setting defaulet values in init method
class Car:
    def __init__(self,brand,price=100):
       self.brand=brand;
       self.price=price;

c1=Car("BMW")
c2=Car("Audi")
print("brand is ",c1.brand," and price of car is ",c1.price,"\n")
print("brand is ",c2.brand," and price of car is ",c2.price,"\n")


 