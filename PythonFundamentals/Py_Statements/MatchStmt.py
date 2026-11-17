##The match statement we use it to void multiple if else statement
##It similar to switch statement
day=4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")  

##Default value:if no case matches then we need to put default value
x=10
match x:
    case 1:
        print("its one")
    case 5:
        print("its two")
    case 9:
        print("its nine")
    case _:            
        print("Looking forward for the weekend")
# Combine Values: using the pipe | character as an operator in the case evalution to check for more than one value match in one case
day=3
match day:
    case 1|2|3|4|5:
        print("Today is rest day")
    case 9|10:
        print("Today is wlaking day")
# If Statements as Guards
month=5                                          
day=4
match day:
    case 1|2|3|4|5 if month==4:
        print("Best day and month of the year")
    case 7|8|9 if month ==5:
        print("Awesome month and day")
    case _:
        print("No criteria matches")    
     
