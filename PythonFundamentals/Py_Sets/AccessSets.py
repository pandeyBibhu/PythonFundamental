###we cannot access items from sets using index value and keys.
#But we can loop through sets items using a for loop

fruiSet={"Apple","Mango","Orange","Papaya","Pineapple"}
for x in fruiSet:
    print(x);

##check if specific value present in the set

for x in fruiSet:
    if "Banana" in x:
        print("Yes Banana is present")
    else:
        print("Not available")
        break;