##Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
thisTuple=("Bibhu","Richa","Jayant","Niti","Akhileshwar","Sandhya","Dakshit","Nishchay","Shreedha")

print("\n-----------Access using Index[]----------------\n")
print(thisTuple[1])
print(thisTuple[2])
print(thisTuple[3])
print(thisTuple[4])

###Negative Indexing

print("\n-----------Access using Negative Indexing[]----------------\n")
print(thisTuple[-1])
print(thisTuple[-2])
print(thisTuple[-3])
print(thisTuple[-4])

###Range of Indexes

print("\n-----------Access using range of Index[]----------------\n")
print("\n",thisTuple[1:3],"\n")
print("\n",thisTuple[2:5],"\n")
print("\n",thisTuple[3:6],"\n")
print("\n",thisTuple[4:6],"\n")
print("\n",thisTuple[:3],"\n")
print("\n-----------Access using range of negative Index[]----------------\n")
print("\n",thisTuple[-1:-3],"\n")
print("\n",thisTuple[-2:-5],"\n")

##check If Item Exist

myTuple=("Apple","Banana","Mango")
print("\n",myTuple,"\n")
if "Apple" in myTuple:
    print("Yes,Its Available")