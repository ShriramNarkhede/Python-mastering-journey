print("enter two numbers ")
n1=input()
n2=input()

try:
    print("Sum of these two numbers is ",int(n1)+int(n2))
except ValueError as e:
    print(e) 
finally:
    print("hoooooooooooooooooooooo")



# print("thank you")   

# def fact(num):
#     if num<1:
#         return 1
#     else:
#         return num*fact(num-1)
    
# i=int(input())
# print(fact(i))
# print(20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)

i,l=0,1
im=int(input("enter::"))

for i in range(2,im):
    im=im+1
    