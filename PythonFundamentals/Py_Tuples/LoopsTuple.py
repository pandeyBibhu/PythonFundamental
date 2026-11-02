print("\n-------Looping the TUples---------------\n")

fruitTuple=("Apple","Banana","Grapes","Orange")

print("\n------for Loop-------------------\n")
for x in fruitTuple:
    print(x)


print("\n-------Loop through Index number---------------\n")

for x in range(len(fruitTuple)):
    print(fruitTuple[x])

print("\n----------While loop-----------\n")
i=0;
while i < len(fruitTuple):
    print(fruitTuple[i])
    i+=1;