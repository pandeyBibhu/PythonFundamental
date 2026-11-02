###List objects have SORT() method that will sort the list alphanumerically,ascending by default
fruitList=["apple","mango","cherry","orange"]
vegList=["potato","tomato","onion","cabagge"]
numList=[10,30,20,40,35,25]
alphanumericList=["apple",20,"Bibhu",30,"Richa",40]

print("\n-----------Sorting Alpha list-------------\n")
fruitList.sort();
for x in fruitList:
    print(x)

print("\n-------------Sorting numbers-------------------\n")
numList.sort();
for x in numList:
    print(x);


# print("\n-------------Sorting alphanumeric-------------------\n")
# alphanumericList.sort();
# for x in alphanumericList:
#     print(x);

##Sorting in Descending order
#To sort in descending  use the keyword argument "reverse=True"
print("\n-------------Sorting numbers into descending order------------\n")
numList.sort(reverse=True)
for x in numList:
    print(x)

print("\n-----------Sorting Alpha into Descending order-------------\n")
vegList.sort(reverse=True)
for x in vegList:
    print(x)

##Customize sort function
#we can also sort the function using keyword argument key=function
#the function will return a number that will be used to sort the list(lowest number first)

print("\n----------Sorting using customize function-------------\n")

def myfunction(n):
    return abs(n-50);

numList.sort(key=myfunction)
for x in numList:
    print(x)

##Case Insensitive Sort:
# Capital letter will get prioritize first by default while using sort method for character or string
print("\n---------------Sorting using case insensitive sort--------------\n")
thisList=["banana","Mango","chana","Borewell"]
thisList.sort();
for x in thisList:
    print(x)

##using key function we can sort this as alphabetically by converting to lower or upper case
print("\n---------Sorting using key=function by alphabetically order-------------\n")
thisList.sort(key=str.lower)
for x in thisList:
    print(x)         

##Reverse the Order of list
#using Reverse() methode we can sort the current order of the element
print("\n--------Before reverse----------------\n")
print(thisList)
print("\n--------------reverse() order of elements---------------\n")
thisList.reverse()
print(thisList)
