###else block is executed once if and elif condition got in return as false.

a=20;
b=30;
if b>a:
    print("b greater than a")
else:
    print("a is greater than b")

#else without elif
# 
x=10;
y=5;
if b>a:
    print("y greater than x")
elif x==y:
    print("both are equal")
else:
    print("x is greater than y")    

# Else as Fallback
# The else statement acts as a fallback that executes when none of the preceding conditions are true. 
# This makes it useful for error handling, validation, and providing default values.


username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")