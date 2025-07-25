# import math

# print("enter number for its multipication table ")
# n=int(input())

# # for i in range (1,11): 
# #      print(n,"X",i,"=",i*n)


# print(5**5)



l = 1
u = 100

for n in range(l,u+1):
    if n > 1:
        for i in range(2,n):
            if(n%i) == 0:
                break
        else:
            print(n)