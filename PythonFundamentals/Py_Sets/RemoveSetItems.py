###To remove items from Sets we can use remove() or discard()

print("\n---------Remove() from sets-----------------\n")
fruitSet={"Apple","Mango","Banana","Orange"}
print("----------before remove--------------")
print(fruitSet)
print("\n---------After remove-------------\n")
fruitSet.remove("Apple")
print(fruitSet)

print("\n---------Discard() from sets-----------------\n")
print("----------before Discard--------------")
print(fruitSet)
print("\n---------After Discard-------------\n")
fruitSet.discard("Apple")
print(fruitSet)

##clear() :empty the set
##we can also use Pop() to remove the items from sets.But not sure which item will get removed.
#Since Sets are unordered collection

##Del keyword use to remove the set completely
delSet={"Aaj","Kal","Parso"}
print(delSet)
del delSet;
print(delSet)