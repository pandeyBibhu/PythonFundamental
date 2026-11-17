#Class:
#Class is a blueprint used to create objects.It defines the properties and behaviours that the object will have.
#These attributes and methods can be accessed using dot notation.

#Object:
#Object is an instance of class.It represent a real world entity and contains its own data along with the methods define in the class.

##IN pyhton everything is object with its properties and methods.
##A object is like object constructor,or blue print for creating objects.

##Create class
print("\n--------creating classess and objects-------------\n")
class firstclass:
    number=10;
#Creating objects:
obj=firstclass();
print(obj.number);

##Delete objects :we can delete del keyword

# del obj;

# print(obj)

#Multiple objects
p1=firstclass();
p2=firstclass();
p3=firstclass();

print(p1.number)
print(p2.number)
print(p3.number)

class employee:
    pass;