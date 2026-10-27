##String Format

age=36
# txt="My Name is jhon,and My age is "+age##this will produce error
## F String :using this we can concatenate int with String
txt2=f"My name is Jhon and My age is {age}"
print(txt2)

##Placeholder and modifiers
#A placeholder can contain varible,function,operation and Modifiers to format the value

price=90
txt3=f"I am apple and price per kg is {price}"
print(txt3)

price2 = 59
txt4 = f"The price is {price2:.2f} dollars"
print(txt4)