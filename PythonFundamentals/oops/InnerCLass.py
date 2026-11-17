#A class define within the class is called inner class.
#Inner class can access properties and method of outer classess.
# Inner classes are useful for grouping classes that are only used in one place, making your code more organized

class Outer:
    def __init__(self):
        self.name="Outer class";
    class Inner:
        def __init__(self):
            self.name="Inner class";
        def display(self):
            print("This is Inner class!!!")
outer=Outer();
print(outer.name)    
##Access Inner class from outer class
inner=outer.Inner();
inner.display()        

# Accessing Outer Class from Inner Class:
#If you need to access the outer class properties from inner class then you have to pass outer class as prameter in inner class.

class Outer:
    def __init__(self):
        self.name="Bibu"
    class Inner:
        def __init__(self,outer):
            self.outer=outer;
        def display(self):
            print(f"outer class name ",self.outer.name)

outer=Outer()
inner=Outer.Inner(outer)
inner.display()


###Practicle Example:
class Car:
    def __init__(self,brand,model):
          self.brand=brand;
          self.model=model;
          self.engine=self.Engine();
    class Engine:
        def __init__(self):
            self.status="off";
        def start(self):
            self.status="Running";
            print("Enginer Started ")
        def stop(self):
            self.status="off"
            print("Engine stopped")
    def drive(self):
        if self.engine.status=="Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car=Car("Toyota","Corolla")
car.drive();                        
car.engine.start();
car.drive();

##Multiple Inner classes:

class Computer:
    def __init__(self):
        self.cpu=self.CPU();
        self.ram=self.RAM();
    class CPU:
        def process(self):
            print("Processing data")
    class RAM:
        def store(self):
            print("storing data")
computer=Computer()
computer.cpu.process();
computer.ram.store();                    