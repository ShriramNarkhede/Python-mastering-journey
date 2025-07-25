import pandas as p
import numpy  as np

li=[1,2,3,4,555]
tp=tuple(li)
l1=list(tp)


di={"name":["ram","lily","shree"],"roll_no":[88,33,11],"marks":[99,98,999]}


#data=np.array([2,3],[5,6])


#print(p.Series(list(di)))

print("Sr_no",p.DataFrame(di))