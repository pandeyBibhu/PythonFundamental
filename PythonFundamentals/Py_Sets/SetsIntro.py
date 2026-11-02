##Sets:
#Its used to store the multiple item into single varible
#A set is collection which is unordered,unchangable and unindexed
#Sets are unchangable but we can add and Remove items from sets.
#sets are written in currly brackets.

##Create a set
print("\n-----------Creating set------------\n")
mySet={"Apple","Mango","Banana","Pineapple"}
print(mySet)
print(type(mySet))

#Sets are unordered Hence we cannot be sure when and How Items will appear
#Sets items are unordered,Unchangeble and do not allow duplicate values
#Items in sets are unordered.
#Sets items are Unchangable ,means we cannot change the items after the sets has been created
#Once set is created we cannot change its items but you can remove items andAdd new Items.

##Duplicates not allowed

thisSet={"Apple","Banana","Apple","Banana"}
print(thisSet)

thisSet1={"Apple","Banana","Banana",True,False,1,0}
print(thisSet1)

##SLength of Set using len()

print("\n--------length of Sets len()--------------------\n")
print(len(thisSet1))

##Sets items can be of any data type.
#String,int,boolean

print("\n---------Data types--------------\n")
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(set1));
print(type(set2));
print(type(set3));

###Set constructor()
#Set constructor can be used to create the set also

print("\n------Creating set using Set() constructor-----------------\n")
thisSet2=set(("Bibhu","Richa","Jayant","Niti"))
print(thisSet2)
