##append(): add the elements at end of the list

fruitList=["apple","mango","cherry","orange"]
fruitList.append("sweetPotato")
print(fruitList)

##Add a list to a list

vegList=["Potato","Tomato"]

fruitList.append(vegList)

print(fruitList)

##clear():Remove all the elements from the list
vegList.clear()
print(vegList)

#count():it count the number of values with specific value
print(fruitList.count("apple"))

##extend()	Add the elements of a list (or any iterable), to the end of the current list
list1=[10,20,30,40]
vegList.extend(list1);
print(vegList)

##index()	Returns the index of the first element with the specified value

print(list1.index(10))

##insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list