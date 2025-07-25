import pandas as pd
import numpy as np
l=[2,3,4,5,5,6,7,7,8,0]
s = pd.Series([10, 20, 30, 40, 50])
ls=pd.Series(l)
print(s)
print(ls)

#dataframe
data = {"name": ['Alice', 'Bob', 'Charlie', 'David'],
        "age": [25, 30, 35, 40],
        "salery":[35000,45000,80000,57500],
        "city": ['New York', 'Paris', 'London', 'Tokyo']}
        
df = pd.DataFrame(data)
print(df)

#panel


data2 = {'item1': pd.DataFrame(np.random.randn(4, 3)),
        'item2': pd.DataFrame(np.random.randn(4, 2))}

p = pd.Panel(data2, items=['A', 'B', 'C', 'D'], major_axis=[0, 1, 2, 3], minor_axis=[0, 1, 2])

print(p)

