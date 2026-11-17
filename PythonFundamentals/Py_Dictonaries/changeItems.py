##We can change item by referring key name
fruitDict={"name":"Apple",
           "color":"Red",
           "price":100,
           "taste":["sour","sweet","Spicy"]
           }
fruitDict["taste"]="Sweet"
print(fruitDict)

##Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.
fruitDict.update({"price":350})
print(fruitDict)