###Join sets
#There are several ways to join the sets
#Using union() and update():joins all items from both the sets
#union():return new set with all item from both sets

print("\n---------union()-------------\n")
set1={"a","b","c"}
set2={10,20,30}

set3=set1.union(set2)
print(set3)

##We can use | operator
print("\n---------| operator-------------\n")
set4=set1|set2;
print(set4)


###Join Multiple Sets
print("\n--------------Join multiple sets--------------\n")
mySet1={10,20,40,30}
myset2={"Apple","Banana","Mango"}
myset3={"Bibhu","Richa","Jayant","Niti"}
myset4={"Patna","Bettiah","Narkatiaganj"}
myset5=mySet1.union(myset2,myset3,myset4)
print(myset5)

print("\n--------------Join multiple sets using | operator--------------\n")
myset6=mySet1|myset2|myset3|myset4
print(myset6)

###Join a Set and a Tuple
#The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

##Update
#The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.
print("\n-----------update()----------------\n")
set11 = {"a", "b" , "c"}
set22 = {1, 2, 3}

set11.update(set22)
print(set11)

##Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.
print("\n---------Intersection()--------------\n")
dupSet1={"Apple","Mango","Banana","Grapes"}
dupSet2={"Mango","Banana","Lichi","Papaya"}

dupSet3=dupSet1.intersection(dupSet2)

print(dupSet3)
print("\n---------& operator--------------\n")
dupSet4=dupSet1&dupSet2;
print(dupSet4)


##Difference
#The difference() method will return a new set that will contain
#  only the items from the first set that are not present in the other set.
print("\n--------Difference()--------------\n")
difSet1={"apple","google","IBM"}
difSet2={"IBM","google","Dell"}
difset3=difSet1.difference(difSet2)
print(difset3)

print("\n--------(- operator)--------------\n")
difset5=difSet1-difSet2
print(difset5)

###Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
symDifset1 = {"apple", "banana", "cherry"}
symDifset2 = {"google", "microsoft", "apple"}

symDifset3 = symDifset1.symmetric_difference(symDifset2)

print(symDifset3)

symDifset3 = symDifset1 ^ symDifset2
print(symDifset3)