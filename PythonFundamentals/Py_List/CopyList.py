##We cannot copy elements from list directly by typing list1=list2
#To copy the list elements we can use built in Copy() methode
fruitList=["apple","mango","cherry","orange"]
vegList=["potato","tomato","onion","cabagge"]
numList=[10,30,20,40,35,25]

print("\n---------Copy()--------------\n")
vegList=fruitList.copy();
print(vegList)

##Use the list() method
print("\n--------------list() to copy---------------\n")
mylist=list(numList);
print(mylist)

##Use the slice Operator

print("\n-----------slice operator[:]-----------------\n")
newlist=vegList[:]
print(newlist)