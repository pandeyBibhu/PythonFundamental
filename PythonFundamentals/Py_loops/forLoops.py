###for loops
fruit=["Apple","mango","banana","orange","papya"]
for i in fruit:
    print(i)


# Looping Through a String
print("\n-------------Printing each character---------------\n")
empName="Bibhu";
for c in empName:
    print(c);  

#Break statement
print("\n----------Break statement----------\n")
myList=["Bibhu","Richa","Jayant","Niti","Akhileshwar","Sandhya"]
for string in myList:  
    print(string)
    if string=="Jayant":
        break;

###continue statement
print("\n---------Continue statement--------------\n")
mytuple=("Bibhu","Richa","Jayant","Niti","Akhileshwar","Sandhya","Dakshit","Nishchay")
for x in mytuple:
    
    if(x=="Niti"):
        continue;
    print(x)

###range()
print("\n-------Range function()-------------\n")
for x in range(1,11):
    print(x)    

# Else in For Loop
print("\n-------else in for loop--------------\n")
for x in range(10):
    print(x)
else:
    print("Finished")

###Nested loops
print("\n-----nested looops---------\n")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
###pass Statement
for x in fruits:
    pass;
