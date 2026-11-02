##Dictonary are used to store the Data into key-value pairs
#A dictonaries is collection which is ordered,changable and do not allow duplicates
#Since python 3.7 dictonaries are ordered and previous version it was unordered.

# dictonaries are written in currly brackets and have key value pair.

empDict={"name":"Bibhu",
         "empId":"101",
         "empLoc":"Bangalore"
         }
print("\n",empDict,"\n");

##Items:
#1:Items are ordered,changable and do not allow duplicates.
#2:it is presented in key value pair and can be reffered to by using the key name.

print("\nEmployeeName: ",empDict["name"])
print("\nEmployeeId:",empDict["empId"])
print("\nEmployeeLocation: ",empDict["empLoc"],"\n")

##Changeable
#Dictionaries are changeable, meaning that we can change,
#add or remove items after the dictionary has been created.

###Duplicates not allowed
#It doesn't allow duplicate keys

thisDict={"fruitName":"Apple",
          "price":100,
          "weight":"1 KG",
          "price":200
          }

print("\n",thisDict)

###Length
#We can find the length of Dictonaries by len().
print("Length of Dict: ",len(thisDict))

##Dictonary items- Data types
#The value in the dictonary items can be any data type

thisDict2={"name":"Bibhu",
           "number":101,
           "location":"Bangalore",
           "subjects":["Phy","chem","Mat"],
           "isGap":True
           }
print("\n",thisDict2)


##type():
print("\n",type(thisDict2))

##dict() Constructor:
#it is use to create a dictonary using brackets

thisDict3=dict(name="Bibhu",age=10,location="Bangalore")
print(thisDict3,"\n")