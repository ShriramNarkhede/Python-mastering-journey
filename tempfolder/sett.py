# s1 = {'friday', 'monday', 'sunday'}

# # check if all elements are true
# result = enumerate(s1)
# print(list(result))


# # Output: True
# languages = ['Python', 'Java', 'JavaScript']

# enumerate_prime = enumerate(languages)

# # convert enumerate object to list
# print(list(enumerate_prime))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
# first set
A = {1, 3, 5,4,0}
# second set
B = {0, 2, 4}
# A.update(B)
# print(A)
# A.update(B)
# print("sorted :::",sorted(A))
# print("after update func",A)
# pp=B.pop()
# cp=B.pop()
# print("pppp",pp)
# print("pppp",cp)
# A.union(B)
# perform union operation using |
c=A - B
print('intersection |:',c )

l=[2,3,4,]
# perform union operation using union()
print('Union using union():', A.union(B)) 