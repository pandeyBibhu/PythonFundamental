##Access Items
#List items are indexed and you can access them by referring to the index number
thisList=["apple","Banana","Mango","Pineapple"]
print(thisList[3])

#Negative Indexing:It means start from end
print("========Negative INdexing==========")
print("\n",thisList[-1])
print("\n",thisList[-2])
print("\n",thisList[-3])

##Ranges of INdexes:
#we can specify a range of indexes by specifying where to start and where to end the range
#When specifying the range,the return value will be new list with specified items

fruitList=["apple","orange","mango","Lemon"]
print("\n",fruitList[1:3])
print("\n",fruitList[:3])

#Range of Negative indexes
print("\n",fruitList[-3:-1])

#check if Item Exist
if "apple" in fruitList:
    print("\n yes,Its available");
    