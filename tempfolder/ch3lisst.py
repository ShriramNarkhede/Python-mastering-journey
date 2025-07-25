l=[]
# v=l.pop(2)
# print(v)
# l.remove(9)
# l[0]=99
# l.insert(0,69)
# l.sort()

for i in range(len(l)):
    pass
    #print(l[i])
    
stri="djdsjsdjds"
lii=list(stri)
print(lii)
print("x" in lii)

print(sorted(l))
print(any(l))
print(l)

a=[1,4,3,6,8]
a.append(99)
a.reverse()
print(a)

evnn=[]
for i in range(0,11):
    if i%2==0:
      evnn.append(i)

print(evnn)

t=(10,20,30,40,50)
t1=(30,49,74,2,4)

print("((((()))))",tuple(t1))
print(len(t))


settt={7,77,7,97}
s={5,6,7,4,55}
print(settt)
settt.add(8888)
settt.add(69999)
settt.discard(7)
settt.update([9,6,4,3,2,0])  

print(settt.difference(s))