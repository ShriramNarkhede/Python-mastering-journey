# print("enter 3 number :")
# a=int(input())
# b=int(input())
# c=int(input())

# if a>b and a>c:
#     print("a is bigger ")
# elif b>a and b>c:
#     print("b is bigger ")
# else:
#     print("c is bigger ")
#   #  print("similler ")
# # else:

def swap(a,b):
    temp=0
    temp=a
    a=b
    b=temp
    print(a,b)

#swap(2,9)
def leap(y):
    if y%4==0 and y%400==0 and  y%4!=100:
        print("leap year :")
    else:
        print("not leap")  

leap(4000)

tup = (('a', 1) ,('f', 2), ('g', 3))
s={('a', 1) ,('f', 2), ('g', 3)}
p=dict(s)
print(p)

m=99
import math
f=math.exp(8)
print(8**2)
print(math.gcd(56,64,72))

import itertools
a=[3,5,2,7,8,99]
print(list(itertools.combinations(a,1)))