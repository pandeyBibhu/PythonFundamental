#IN python we have multiple data types
#Python has Different built in DataTypes

#1:Text type => str
#2:Numeric Types=> int,float,complex
#3:Sequence Types=>list,tuple,range
#4:Mapping types: dict
#5:Set types: set,frozenSet
#6:Boolean types:bool
#7:Binary types:bytes,bytearray,memoryView
#8:NonTypes: NoneType

#Getting the Data Type
#we can use the  function type() to retrive the data types

x="Bibhu Pandey"
print(type(x))

#Setting the data Type
#We set the Data Type when we assing the value to the varible

x="Bibhu Pandey";#String 
print(type(x))
y=20; #int
print(type(y))
z=20.6;#float
print(type(z))
a=1j;#complex
print(type(a))
b=["Apple","Mango","Banana"];#list
print(type(b))
c=("Apple","Mango","Pineapple");#tupple
print(type(c))
d=range(6);#range
print(type(d))
e={"name":"Bibhu","age":40};#dict
print(type(e))
f={"Apple","Banana","Cherry"};#set
print(type(f))
g=frozenset({"Apple","Guava","Papaya"})
print(type(g))
h=True;#bool
print(type(h))
k=b"Hello"#bytes
print(type(k))
l=bytearray(5);#bytearray
print(type(l))
m=memoryview(bytes(5));#memoryview
print(type(m))
n=None ;#non type
print(type(n))


##SETTING the Specific Data type
print("----------------Setting the Speccific data types--------------------")
xx=str("Bibhu Pandey")
print(type(xx));

yy=int(30)
print(type(yy));

zz=float(30.4)
print(type(zz))

aa=complex(3j)
print(type(3j))

bb=list(("Bibhu","Richa","Jayant","Niti","Sandhya","Akhuleshwar"))
print(type(bb))

cc=tuple(("Bibhu","Richa","Jayant","Niti","Sandhya","Akhuleshwar"))
print(cc)

dd=range(7)
print(dd)

ee=dict(name="Jayant",Age=40)
print(type(ee))