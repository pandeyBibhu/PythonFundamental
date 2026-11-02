##Append Items:
#To add the item at the end of list,we can use append()

fruitList=["apple","mango","pineapple","orange"]

print("\n---------Before Append------------\n")
print(fruitList)
print("\n---------After Append------------")

fruitList.append("cherry")
print(fruitList)


##Insert Items
#To add or insert an item at specified index we can use insert()
fruitList[3]="Lemon"
print("\n**************After insert*************")
print(fruitList)

##Extend List:
# To add items from another list to current list,use the extend() method

vegList=["potato","tomato","cauliflower","cucumber"]
print("\n------Before Extend--------")
print(vegList)
vegList.extend(fruitList)
print("\n-----------After Extend-------------")
print(vegList)

##Add any Iterable
thistuple = ("kiwi", "orange")
vegList.extend(thistuple)
print("\n",vegList)


##Remove List Items