# -*- coding: utf-8 -*-
"""Python Operator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Ow2FA6xbToXGR6zvqYoHy5abylWBRqh
"""

print(11%3)

x=3
y=5
x+=y
print(x)

x=3
y=5
x-=y
print(x)

x=3
y=5
x*=y
print(x)

x=3
y=5
x/=y
print(x)

x=11
y=3
x%=y
print(x)

#Exponent
x=2
y=3
x**=y
print(x)

#Flore Division
x=7
y=2
x//=y
print(x)

a = 9
b = 10
c = a&b
print((c))
print(bin(c))

a = 9
b = 10
c = a|b
print((c))
print(bin(c))

a = 9
b = 10
c = a^b
print((c))
print(bin(c))

a = 9
c = ~a
print(bin(c))

#Binary Left Shift
a = 9
c = c<<2
print((c))
print(bin(c))

#Binary Right Shift
a = 9
c = c>>2
print((c))
print(bin(c))

#List Manipulation
list=[1,2,3,4,5,6]
if(2 in list):
  print("2 exist in the list")
else:
    print("2 does not exist in the list")

#List Manipulation
list=[1,2,3,4,5,6]
if(20 in list):
  print("20 exist in the list")
else:
    print("20 does not exist in the list")

a = 20
b = 20
 
if ( a is b ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")

a = 20
b = 21
 
if ( a is not b ):
   print ("a and b have different identity")
else:
   print ("a and b do have same identity")