# li=[2,4,5,6,7,8,3,4,66]
# for i in range(li[0],li.__sizeof__()):
#     print(li[i])
# i=0
# while i!=10:
#     print(i!=10)
#     continue
#     i=i+1
l = 1
u = 100

# for n in range(l,u+1):
#     if n > 1:
#         for i in range(2,n):
#             if(n%i) == 0:
#                 break
#         else:print(n)
while True:
    num=int(input("enter num :"))
    if ((num%2) == 0  or num==1) and (num !=2):
        print(num,"is not prime number")
    else: print(num,"is prime number")
