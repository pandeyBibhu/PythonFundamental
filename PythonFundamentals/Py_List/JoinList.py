##Join two list
##There are many ways to join two list or concanate or mor list in python.
#The easiest way is using "+" operator

fruitList=["apple","mango","cherry","orange"]
vegList=["potato","tomato","onion","cabagge"]
numList=[10,30,20,40,35,25]

print("\n----------using '+' operator-----------\n")
newList=fruitList+vegList;
print(newList)
for x in newList:
    print(x)

##Join using append()
print("\n------------Join using append()-----------------\n")
for x in numList:
    vegList.append(x)

print(vegList)   

##Join using extend()
print("\n--------join using extend()---------------\n")
fruitList.extend(vegList);
print(fruitList)
