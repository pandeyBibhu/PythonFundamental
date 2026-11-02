###Identiity operator is used to compare the objects,not if they are equal but if they are actually same object
##with same memory location

x=[10,20,30]
y=[10,20,30]
z=x;

print(x is y)
print(x is z)
print(x == y)
print(z is x)

print(x is not y)