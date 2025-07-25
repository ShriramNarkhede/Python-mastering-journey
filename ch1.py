# a,b=0,1
#n=int(input("enterrrr....:"))
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")

# def f(n):
#     if n<=1:
#         return 1
#     else:
#         return n*f(n-1)
# print(f(n))
# i=0
# for i in range (0,n):
#     for j in range(0,i):
#         print(i,end=" ")



# #     print("")  
# a=False
# print(('not a is',not a))

# for i in range(0,5):
#     for j in range (1,i+1):
#       print(j,end=" ")

#     print("")

# d={4:"trtr",5:"rururur",6:"hxhxx"}
# d.update({4:"ram"})
# print(d)
# l=[]
# for i in range (0,4):
#     i=int(input("enter elements:for tuple 1,..."))
#     l.append(i)

# l2=[]
# for i in range (0,4):
#     i=int(input("enter elements:for tuple 2,..."))
#     l2.append(i)

# # print(l)
# # print(max(l))
# t1=tuple(l)
# t2=tuple(l2)
# print("before sswapingg .....")
# print(t1)
# print(t2)

# t3=t2
# t2=t1
# t1=t3
# print("after. sswapingg ......")
# print(t1)
# print(t2)

l=[4,5,6,7]
s={6,7,8,2,0}
s.update(l)
print(s)