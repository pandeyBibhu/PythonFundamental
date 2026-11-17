fruitDict2={"name":"orange",
            "price":350,
            "color":"red"
            }

for x in fruitDict2:
    print(x)#this will return only keys available in dictonaries
    print(fruitDict2[x])#this will return only values available in the dictonaries

    ##values()

for x in fruitDict2.values():
    print(x)  

for x in fruitDict2.keys():
    print(x)

##loop through both key and value
for x,y in fruitDict2.items():
     print(x,y)