##Basically we have three type of Numbers in python
#1:int 2:float 3:complex

#varibles of Numerics types decides when you assign the values to varible

x=10;#int
print(x,type(x))

y=10.3;
print(y,type(y))

z=7j
print(7j,type(z))

#Convert from one type to another type

print("-------Convert from int to float------------");
a=float(x)
print(a,type(a))

print("-------------Convert from float to int------------")
b=int(y)
print(b,type(b))

print("---------------Convert from int to complex------------")
c=complex(z)
print(c,type(c))


#Random number

#python does not have function called randon().But it has in built module called random  that can be used to make random number
print("========Random Number==============")
import random
print(random.randrange(1,10000))