from abc import ABC,abstractmethod
class color(ABC):
    @abstractmethod
    def mycolor(self):
        pass
class green(color):
    def mycolor(self):
        print("greeen")
class red(color):
    def mycolor(self):
      print("red")

r=green()
r.mycolor()
        