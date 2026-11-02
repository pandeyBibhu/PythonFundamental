###List are used to store the multiple item in single varible
#List is used to store the collection of data from List,tuple,set,Dictonary
#All with different qualities and qualities
#List can be created using square bracket.

print("========Create list==========")
List=["one","two","three","four"]
print(List)

##List Items:List items are indexed and 
# It can be accessed using based on indexed value and it store item on indexed basis.
#List item are ordered and It can be changed and It allow duplocate values
#If you add any element in the list that will get added at the end of list items
#Changable means,we can add,remove and update the list items once list is created.

print("\n=============Allow duplicate value===========");
list2=["one","two","Three","Four","one","two","three"]
print(list2)

##len():to find the length of list we can use len()
print("===========len()============")
print(len(list2))

##list Items can be any data types
print("\n===========Data TYeps of Items=============")
li1=["Bibhu","Richa"]
li2=[1,2]
li3=[True,False]
print("\n",li1,"\n",li2,"\n",li3);

##A list can contain different data types

li4=["abc",23,"True",30,"male"]
print("\n",li4);

##type()
print("\n",type(li4));

##List() constructor: Its is used to create new list using list constructor

thislist = list(("apple", "banana", "cherry"))
print(thislist)
