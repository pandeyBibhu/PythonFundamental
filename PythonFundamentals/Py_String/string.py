#String in python are surrounded by single quote or Double quote

print("Bibhu Pandey")
print('Bibhu Pandey')

#Quotes Inside Quotes
print("My name is 'Bibhu'")
print('My name is "Bibhu Pandey"')

#Assign String to a Variable

x="Bibhu Pandey"
print(x)

#Multiline Strings

y="""Bibhu Kumar Pandey
        from Narkatiaganj
        west champaran Bihar 
        845455"""
print(y)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
string="Bibhu"
print(string[1])
#looping and extracting each character
for i in string:
    print(i)

#String length len()
print(len(string))  

##Check String:to check phrase or character present in given string we use keyword in
txt="My name is bibhu kumar pandey from Bihar";
print("Bihar" in txt);
print("Bihari" in txt);

##use If statement

if "Bihar" in txt:
    print("yes,'Present'")

##Check if Not:To check if certain phrase is not present in a string,we can use the keyword "not in"
print("Bihari" not in txt);
print("Bihar" not in txt);

##Print only if expensive no present in txt

if "Bihari" not in txt:
    print("Yes ,Its 'not present'")
    