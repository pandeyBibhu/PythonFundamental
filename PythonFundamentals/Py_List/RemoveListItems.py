##Remove List Items
#To remove any item we can use remove methode
placeList=["Patna","Bettiah","Narkatiaganj","motihari","Narkatiaganj","motihari"]
print("\n-------------Before remove-------------\n")
print(placeList,"\n")
print("\n-------------After remove-------------\n")
placeList.remove("Patna");
print(placeList,"\n")

#If there are more than one item with the specified value, the remove() method removes the first occurrence
placeList.remove("Narkatiaganj")
print("\n",placeList,"\n")


##Remove Specified Index
#The pop() method removes the specified index
placeList.pop(1);
print("\n",placeList,"\n")

##If you do not specify the index, the pop() method removes the last item.
placeList.pop()
print("\n",placeList,"\n")

##The del keyword also removes the specified index:
del placeList[0]
print("\n",placeList,"\n")


##Clear the List
placeList.insert(2,"Bagaha")
placeList.insert(3,"Ramnagar")
placeList.insert(4,"Valmikinagar")
print("\n---------Before clearing the list-----------\n")
print("\n",placeList,"\n")

print("\n---------After clearing the list-----------\n")
placeList.clear();
print("\n",placeList,"\n")

