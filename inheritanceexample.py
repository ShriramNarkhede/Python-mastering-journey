class a:
    #   roll=11
      def __init__(self,name,rollno):
           print(name)
           print(rollno)


class c(a):
         def __init__(self):
               print("ssss")
               
                
        
        

class b(c):
    # name="shree"
    def __init__(self) :
        # print(self.name)
        # print(self.roll)
        a.__init__(self,"shreeram",699)
        c.__init__
        

        
bc=b()
    