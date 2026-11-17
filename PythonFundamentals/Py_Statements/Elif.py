##Elif conditin check if previous condition were not true then try this condition

a=20
b=24
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")


###Multiple Elif statements    
print("\n---------Multiple Elif statements-------------\n")
score=75;
score = 75

if score >= 90:
    print("Distinction")
elif score >= 60:
    print("First division")
elif score > 30:
    print("Second class")
elif score == 30:
    print("You are just passed")
else:
    print("Please try again!!")
