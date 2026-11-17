##POLYMORPHISM:
#Polymorphism means same method to be used in diffrent claas with same name
#We can achive polymorphism by using duck typing and By using Inheritence
#Polymorphism using duck typing:
class Boat:
    def __init__(self,brand,model):
                self.brand=brand;
                self.model=model;
    def move(self):
          print("Sail!!!")
class car:
         def __init__(self,brand,model):
                         self.brand=brand;
                         self.model=model;
         def move(self):
                   print("Running!!!")       
class Plane:
         def __init__(self,brand,model):
                         self.brand=brand;
                         self.model=model;
         def move(self):
                   print("Flying!!!")
b1=Boat("Cruise","2025")
c1=car("Nexon","2026");
p1=Plane("Boeing",747)

for x in (b1,c1,p1):
        x.move();

###Using Inheritence Polymorphism:
print("\n---------Inheritence Polymorphism------------\n")
class Animal:
        def __init__(self,name):
                self.name=name;
        def voice(self):
                print("Speaking!!!!")

class Dog(Animal):
        def __init__(self, name):
                super().__init__(name);
        def voice(self):
                print("Barking!!!!")
class Cow(Animal):
        def __init__(self, name):
                super().__init__(name)
        def voice(self):
                print("Cowing!!!!!")
class Cat(Animal):
        def __init__(self, name):
                super().__init__(name)
        def voice(self):
                print("Meowing!!!!")
d1=Dog("Zerman Shepared")
c1=Cow("Jarshi")
c2=Cat("Catty")
for x in (d1,c1,c2):
        print(x.name);
        x.voice();                                        
