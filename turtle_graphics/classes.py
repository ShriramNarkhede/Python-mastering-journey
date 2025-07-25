class student:
 def __init__(self,rollno,name,age):
      self.rollno=rollno 
      self.name=name
      self.age=age
      print("student object is created")
      
p1=student(11,"Ajay",20)
print("Roll No of student= ",p1.rollno)
print("Name No of student= ",p1.name)
print("Age No of student= ",p1.age)