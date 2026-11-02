x=5
print(x)

x+=2;
print(x)
x-=2;
print(x)
x*=2;
print(x);

x/=2;
print(x)

x%=2;
print(x);

x//=2;
print(x)

x**=2;
print(x);

# x&=2;
# print(x);

# x|=2
# print(x)

# x^=2;
# print(x);

# x>>=2;
# print(x)

# x<<=2
# print(x)

## The Warlus operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")