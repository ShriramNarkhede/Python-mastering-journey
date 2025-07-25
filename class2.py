class ram:
    def bb(self,n):
        print("sgdghd",n)

class __shree(ram):
    _pro_myname="shreeram"
    __pri_myno=30
    def __init__(self):
        print("abc")  
    def abc(self,n,ro):
        super().bb(n)
        r=ram()
        r.bb(9999)
        
 

obj=__shree()
obj.abc(77,99)
print(type(obj))
obj.__init__()
#print(obj._shree__pri_myno)
print(obj._pro_myname)


