###Once tuple is create It cannot be chenged and Updated and deleted.Its called immutable
##But There is some workaround to update or change the Tuple values

#1:Change the Tuple values by converting into List and converting back to tuple

#Step:1:Creating the Tuple
myNameTuple=("Bibhu","Richa","Jayant","Niti","Akhileshwar","Sandhya")
print(myNameTuple)

#Step:2:Converting tuple into List

myList=list(myNameTuple);
print(myList)

#Step:3:Updating List

myList[5]="Dakshit"
myList[4]="Nishchay"
myList[3]="Shreedha"

print(myList)

#Step:4:Converting back tuple
myNameTuple=tuple(myList)
print(myNameTuple);

###Add Items
#Since we cannot update or change the tuple,Hence we can converting into List 

myAddList=list(myNameTuple)
myAddList.append("Akhileshwar")
myAddList.append("Sandhya")
print(myAddList)
myNameTuple=tuple(myAddList)
print(myNameTuple)

##. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

addTuple1=("Iksha",)
myNameTuple +=addTuple1;

print(myNameTuple)

##Remove Items

removeList=list(myNameTuple)
removeList.remove("Iksha");
myNameTuple=tuple(removeList);
print(myNameTuple)

###del keyword
#It is used to delete the tuple completely

delTuple=("Jeena","Peena","Kheena")
del delTuple
print(delTuple)