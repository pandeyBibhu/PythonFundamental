#capitalize(): convert the first character to upper case
print("==============capitalize()================");
string="bibhu kumar pandey";
print(string.capitalize())

##caseFold():Convert the string into Lower case
print("==============casefold()================");
string1="bibhu";
print(string1.casefold());

##center():Return a centered string
print("============center()=============")
print(string1.center(10))

##count()	Returns the number of times a specified value occurs in a string

print("=============count()===============")
print(string1.count("bi"))

txt="I like Apple,Apple is my favriote fruit.";
print(txt.count("Apple"))
print(txt.count("i"))

##endswith():Returns true if the string ends with the specified value
print("=============endswith()===============")
print(txt.endswith('.'))
print(txt.endswith('it.'))
print(txt.endswith('k',1,5))
x = txt.endswith(("world.", "castle."))

print(x)


##find():Finds the first occurance of the Specied value.
#return -1 if not found
print("\n============find()==================\n")
txt2="Hello world,Welcome to my world"
y=txt2.find("Hello")
print(y);
print(txt2.find("world"))
print(txt2.find("Welcome"))
print(txt2.find("e"))
print(txt2.find("l"))
print(txt2.find("o"))
print(txt2.find('l',1,5))
print(txt2.find('e',1,20))

##isDigit():check if all the character in the string are digit
print("\n=======isDigit()===========")
num="345780";
print(num.isdigit())

num2="345780cfa";
print(num2.isdigit())


##index():Searches the string for a specified value and returns the position of where it was found
print("============index()================")
txt4="My name is Apple,and apple is good for heart health"
a=txt4.index("name");
print(a)

a=txt4.index("n");
print(a)
a=txt4.index("m");
print(a)

##isalnum(): return True if all the character in the string is alphanumeric
print("\n=========isalnum()=============")

txt5="Bibhu890"
print(txt5.isalnum())

##isAlpha():return True if all the character in the string is alphabetic
print("\n==================isAlpha()==================")
txt6="bibhu2"
print(txt6.isalpha())

##isAscii():return True if all the character in the string is ascii
print("\n==========isAscii()=============")
txt7="january"
print(txt7.isascii())

##isDecimal()
print("\n==============isDecimal()===============")
txt8="1234.10"
print(txt8.isdecimal())

##isIdentifier()

print("\n==========isIdentifier()==============")
txt9="Demo";
print(txt9.isidentifier())

print("12Bibhu".isidentifier())
print(" bibu".isidentifier())

##isNumeric():
print("\n=========isnumeric()=============")
print("12345678".isnumeric());
print("123Bibhu".isnumeric());