def add(p,q):
      return p*q
def subtract(p,q):
      return p-q
def multiply(p,q):
      return p*q
def divide(p,q):
      return p/q

print("Please select the operation. ")
print("1. Add")
print("2. subtract")
print("3. Multiply")
print("4. Divide")

choice = input("please enter choice (1/ 2/ 3/ 4): ")
num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))

if choice == '1':
      print(num1," + ", num2," = ",add(num1,num2))

elif choice == '2':
       print(num1," - ", num2," = ",subtract(num1,num2))

elif choice == '3': 
      print(num1," * ", num2," = ",multiply(num1,num2))      

elif choice == '4':
      print(num1," / ", num2," = ",divide(num1,num2))

else :
      print(" invalid input ")
