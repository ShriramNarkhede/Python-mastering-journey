def add(p,q):
      return p+q
def subtract(p,q):
      return p-q
def multiply(p,q):
      return p*q
def divide(p,q):
      return p/q
print("------------------------ Faulty Calculator ------------------------")
print("Please select the opration. ")
print("a. Add")
print("b. subtract")
print("c. Multiply")
print("d. Divide")

choice = input("please enter choice (a/ b/ c/ d): ")
num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))

if choice == 'a':
      if num1==56 and num2==9:
          print(num1," + ", num2," = ", "77")
      else :
            print(num1," + ", num2," = ",add(num1,num2))

elif choice == 'b':
       print(num1," - ", num2," = ",subtract(num1,num2))

elif choice == 'c':      
       if num1==45 and num2==3 or num1==3 and num2==45:
          print(num1," * ", num2," = ", "555")
       else :
            print(num1," * ", num2," = ",multiply(num1,num2))    

elif choice == 'd':
      if num1==56 and num2==6:
            print(num1," / ", num2 ," = ", "4")
      else:
            print(num1," / ", num2," = ",divide(num1,num2))

else :
      print(" invalid input ")
