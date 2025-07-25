list1=[1,2,3,4,5,6,99]

#insert 222 value at index 1
list1.insert(1,222)
print("insert 222 at index 1 ",list1)

#replace elements form 2 to 5 index
list1[2:5]=[66,69,88]
list1[2]="shree"#replace element at index 2
print(list1)

#add element in list at end
list1.append(1114)
print(list1)

#pop elemment at given index
popedele=list1.pop(1)
print(list1)
print(popedele)

#sorting
# print(list1.sort())

#delete elemment at index
del list1[0]
print(list1)

#remove 99 value form list
list1.remove(99)
print(list1)


#compairing  lists
list2=[1,2,3,4,5,6,99]
list3=[1,2,3,4,5,6,99]
if(list2==list3):
    print("list2 and list3 is same")
else:
    print("content in both list is different")

#copy value from list 
copiedList=list2.copy()
print("copied list ",copiedList)

#concatenation 
list4=list1+list2
print("concat",list4)

#check that item exist in list or not
print(99 in list4)

lengthoflist4=len(list4)
print("length of list4 ",lengthoflist4)
# #
# for i in list4:
#     print(i)