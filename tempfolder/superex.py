from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def parentp(self,name,no):
        pass

class b(a):
    def chaild1(self, name, no):
      print("my name is :",name,"\n","number :",no)

    def parentp(self,name,no):
          print("shshshjs")

ob=b()
ob.parentp("djdjfjf",878787)
ob.chaild1("shreeram ",3878474)