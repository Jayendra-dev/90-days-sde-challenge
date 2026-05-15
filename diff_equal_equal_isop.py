#Difference between equal-equal and is operator .
a=[1,2,3,4]
c=ord('A')
print(c)
d=chr(68)
print(d)
a1=chr(97)
print(a1)
a2=chr(78)
print(a2)

b=[1,2,3,4]
print(id(a))
print(id(b))
print(a is b)
print(a==b)