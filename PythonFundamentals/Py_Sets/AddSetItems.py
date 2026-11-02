###Once set is creted we cannot changes the Sets but we can add the items
print("\n------------Add item into Set using Add()-------------------\n")
thisSet={"Bibhu","Richa","Jayant","Niti"}
print(thisSet)
thisSet.add("Akhileshwar");
thisSet.add("Sandhya");
print(thisSet)

##AddSets
#To add sets from another sets we can use Update()
print("\n-------Add one set into another set using update()--------------\n")
fruitSet={"Apple","Banana","Mango","Grapes"}
fruitset2={"Papaya","Orange","Pineapple","Cherry"}
fruitSet.update(fruitset2);
print(fruitSet)

#Add Any Iterable
#The object into Sets cannot be only sets,It can be list,tupple or Dictonaries

list=["Potato","Tomoto"]
fruitSet.update(list);
print("\n--------------Adding list into set using update()------------------\n")

print(fruitSet)