##Using for loop we can loop the list

fruitList=["apple","mango","cherry","orange"]
vegList=["potato","tomato","onion","cabagge"]
numList=[10,30,20,40,35,25]

print("\n--------looping numList using for loop---------\n")
for i in numList:
    print(i);
    
print("\n");
##Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
print("\n---------Loop through index number-------------\n")
length=len(fruitList)
for j in range(length):
    print(fruitList[j])

print("\n")    

###While Loop
print("\n-------Using while Loops-------------\n")
size=0
while size < length:
    print(fruitList[size])
    size+=1;
print("\n")

##Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists:
[print(x) for x in vegList]
print("\n")

