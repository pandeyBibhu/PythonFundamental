##we can remove items from dictonaries using POP()
fruitDict={"name":"apple",
           "price":200
           }
fruitDict.pop("price")
print(fruitDict)

##popItem:remove last inserted item

fruitDict2={"name":"orange",
            "price":350,
            "color":"red"
            }
fruitDict2.popitem()
print(fruitDict2)

##del keyword also used to delete the dictonaries.
#once we use del keyword to dictonaries then after that we try to access the dictonaries then it should throw error
del fruitDict2;
print(fruitDict2)