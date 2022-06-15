import math
#ask for inputs
print('a=')
a=int(input())
print('b=')
b=int(input())
print('c=')
c=int(input())
#do the quadratic formula now
if ((b**2+(c*a*(-4))) / -1) > 0:
    print("discriminate is negative, try again")
#if discriminate works then do formula
else :
    x = (-b+(math.sqrt(b**2-(c*a*4))))/(a * 2)

    z = (-b-(math.sqrt(b**2-(c*a*4))))/(a * 2)

    print('x=', z , ',' , x)
