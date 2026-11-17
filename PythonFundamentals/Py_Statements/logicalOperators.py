###Logical operator are used to combine conditional statements
##Python has three logical operators and,or not

##and:
a=30
b=40
c=20

if a>b and c>a:
    print("condition is true")
else:
    print("conditon is false")

###or 
if a>b or c>a:
    print("condition is true")
else:
    print("condition is false") 

###not :used ot reverse the result of conditional statement
if not a>b:
    print("Condition is true")

# Combining Multiple Operators
# when we combine multiple operators in a single expression.
# python evalutes not first,and second,or third

age=25
is_student=True;
has_discount_code=True;

if (age<18 or age>65) and not is_student or has_discount_code:
    print("discount applies!!!")

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")    