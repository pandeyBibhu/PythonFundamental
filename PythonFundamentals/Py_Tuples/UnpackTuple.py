###We normally assign values to tuple while creating the tuple.
#This process is called packing
##And whe we try to extract the values and assign it to varibles is Called Unpacking

fruitsTuple=("Apple","Mango","Grapes","Pineapple")#this is packing

##Now unpacking
(red,yellow,Green,brown)=fruitsTuple
print(red);
print(yellow);
print(Green);
print(brown);


###Using Asterisk*
#When number of varible is less then the number of Values,Then values will be assigned to varible where asterick is applies as list
print("\n-----Using Asterick*---------------\n")
(red,yellow,*Green)=fruitsTuple
print(red)
print(yellow)
print(Green)