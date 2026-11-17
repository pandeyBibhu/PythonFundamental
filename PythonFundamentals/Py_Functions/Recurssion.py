##Recurssion means calling the same function

#recirsive program  that count down from 5
def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)

countdown(5)

##Every recurssion must have base case and recursive case
#Base case is that stop the execution when condition meets
#Recursive case is that keeps executing 

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(6))  

##Find the 7th Fibonacci number in the sequence

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

##Recurssion with List
#Recursion can be used to process lists by handling one element at a time:
myList=[1,2,3,4,5,6]

def sum_list(numbers):
    if len(numbers)==0:
     return 0
    else:
        return numbers[0]+sum_list(numbers[1:])
print(sum_list(myList))   


##Find the maximum value from the list
my_list=[3,2,6,9,7]

def findMaximum(numbers):
    if len(numbers)==1:
        return numbers[0];
    else:
     max=findMaximum(numbers[1:])
     return numbers[0] if numbers[0]>max else max;

print(findMaximum(my_list))

##Recursion depth limit
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
import sys;
print(sys.getrecursionlimit())

##We can set recursion depth limit as well
import sys
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())
    
