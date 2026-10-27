#Casting is done in python using constructor fundctions:
#int():constructs an integer number from an integer literal, 
#      a float literal (by removing all decimals), or 
#      a string literal (providing the string represents a whole number)

x=int(1)
print(x)
y=int(2.8)
print(y)
z=int("34")
print(z)

#float():constructs a float number from an integer literal,
#        a float literal or a string literal (providing the string represents a float or an integer)
x = float(1)     # x will be 1.0
print(x)
y = float(2.8)   # y will be 2.8
print(y)
z = float("3")   # z will be 3.0
print(z)
w = float("4.2") # w will be 4.2
print(w)
#str():constructs a string from a wide variety of data types, 
#      including strings, integer literals and float literals.

x = str("s1") # x will be 's1'
print(x)
y = str(2)    # y will be '2'
print(y)
z = str(3.0)  # z will be '3.0'
print(z)