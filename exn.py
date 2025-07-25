# n=int(input("enterrrr ..."))
# def fact(n):
#     if n<2:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(n))

# a=10
# b=10
# c=a
# tr=(9,5,8,5,3)

# print(a is b)
# class zero(Exception):
#     def __init__(self):
#         print("division by zero error .....")
# print("enterrr 2 num for div....: ")
# i=int(input())
# i1=int(input())
# try:
#     if(i1<1):
#         raise zero
#     else:  
#       print("div is...: ",i/i1)
# except zero as a:
#     print("number can't be divide by zero ..",a)
# s="python programming"
# print(s[10:3:-1])

# Python program to demonstrate
# string slicing
 
# String slicing
String = 'GEEKSFORGEEKS'
 
# # Using indexing sequence
# print(String[1:12:3])

class rect:
    length=0
    breadth=0
    def  __init__(self,l,b):
        self.length=l
        self.breadth=b
    def areawidth(self):
        print(" aera of rectangle is :...",self.length*self.breadth)
        print(" parimeter of rectangle is :...",2*(self.length*self.breadth))

# c=rect(8,9)
# c.areawidth()
a={1,2,3,4}
b={4,5,6}

# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)
# print(a.symmetric_difference(b))
# print(a.isdisjoint(b))

def calculate_area(side_length):
    return side_length * side_length

def calculate_area(length, width):
    return length * width

# Calculate the area of a cube
cube_side_length = 5
cube_area = calculate_area(cube_side_length)
print("Area of the cube:", cube_area)

# Calculate the area of a rectangle
rectangle_length = 6
rectangle_width = 4
rectangle_area = calculate_area(rectangle_length, rectangle_width)
print("Area of the rectangle:", rectangle_area)