####Python Lamda:
#It is an anonymous function.
#This can take any number of argumnets and here expression executes and values returned
#Syntax: lamda arguments:expression

print("\n----Perform Addition using lamda function---------\n")
x= lambda a:a+10;
print(x(10))

#Multiple arguments using lambda
print("\n-------Perform multiplication using lambda function-------------\n")
mul=lambda a,b:a*b;
print(mul(10,20))

##Summerize the arguments and return the results
print("\n-------Summerize the arguments and return the results------------\n")
add=lambda a,b,c:a+b+c;
print(add(10,20,30))

##Lambda function
print("\n----------lambda functions---------\n")
def myFunction(n):
    return lambda a:a*n;

mydoubler = myFunction(2)
print(mydoubler(11))

mydoubler = myFunction(4)
print(mydoubler(11))

###lambda with builtin function
#lambda function normally used with built in function map(),filter() and sorted()
#using map() with lambda function.

print("\n-----Double all the number in the list------\n")
list1=[1,2,3,4,5,6,7,8,9]
mydouble=list(map(lambda a:a*2,list1))
print(mydouble)

##Using Lambda with filter()
#The filter function creates a list of items for which a function return True
print("\n-----Lambda with filter-----------\n")
myitems=[1,2,3,4,5,6,7,8,9]
mydouble2=list(filter(lambda a:a%2!=0,myitems))
print(mydouble2)


##Using Lambda with sorted()
#The sorted() can be use lambda as key for custom sorting

listSort=[3,2,5,6,1,20,15]
mysort=list(sorted(listSort,key=lambda a:a,reverse=False))
print(mysort)