#varible declared outside the function is known as GLobal varible and It can be accessed by everyone.

x="Awesom"

def myfunc():
    print("Python is "+x);

myfunc()

#The varible is created inside a function is known as Local varible and It will access onlt within the same function

def newFunc():
    x="Fantastic"
    print("python is "+x);

newFunc();
print("Python is "+x)

#global keyword

#when we create a varible inside a function floowing a global keyword
#that will be accessed globally
y="Bibhu Kumar"
def empFunc():
    global y;
    y="Bibhu kumar Pandey";
print("Nice person is "+y)
empFunc();
print("My name is  "+y);

