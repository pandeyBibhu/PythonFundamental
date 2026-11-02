##Boolean return one or two values always either tru or false

print(9>10);
print(10>8);

a=9000;
b=1100;
if b>a:
    print("B is greater")
else:
    print("A is greater")

##bool() function

print(bool(13))
print(bool("Bibhu12"))
print(bool())
print(bool(0))
print(bool(None))
print(bool([]));
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

##function can return boolean value

def Myfunction():
   return True;
print(Myfunction())

### we can execute code based on the Boolean answer of a function:

def myFunction():
   return True;
if myFunction():
   print("YES")
else:
   print("NO")
x = 200
print(isinstance(x, int))