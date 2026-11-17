##if you have only one statement to execute,you can put it on the same line as the if statement

a=10;
b=20;

if a<b:print("b is greater than a")

##shorthand if else

print(a) if a > b else print(b)

# Assign a Value With If ... Else

varible=a if a>b else b
print(varible)

####Multiple condition in one line

x=10
y=20
print(x) if x>y else print("=") if x==y else print(y)

##Using ternary operator

max=x if x>y else y;
print(max)