##List comprehension offer us to write the shorter syntax when you want ot create new list based on 
# the value of existing list
fruitList=["apple","mango","cherry","orange"]
vegList=["potato","tomato","onion","cabagge"]
numList=[10,30,20,40,35,25]

newList=[x for x in fruitList if "apple" in x]
print("\n",newList,"\n")

newList=[x for x in fruitList if "apple" not in x]
print("\n",newList,"\n")

newList=[x for x in fruitList if x!="apple" ]
print("\n",newList,"\n")

newList=[x for x in vegList ]
print("\n",newList,"\n")

newList=[x for x in range(10) ]
print("\n",newList,"\n")

newList=[x for x in range(10) if x<5]
print("\n",newList,"\n")

newList=[x for x in range(10) if x<5]
print("\n",newList,"\n")