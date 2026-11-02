##Change Item Value
#To change the value of specific value we can refer index number

thisList=["apple","banana","cherry","mango"]
thisList[2]="Bibhu"
print(thisList)

#Change a Range of Item Values
thisList[1:3]=["Chandan","Richa"]
print("\n",thisList);
thisList[1:3]=["Chandan","Richa","Dakshit"]
print("\n",thisList);

thisList[1:3]=["Nishchay"]
print("\n",thisList);

##Insert Items:to insert the item in the list we can use insert() with index value

fruitsList=["apple","Banana","Orange","Mango","Cherry"]
print("--------Before Insert------------")
print("\n",fruitsList)
fruitsList.insert(2,"Watermelon")
print("----------After insert----------")
print("\n",fruitsList)

