def fact(num):
      if num ==1:
            return 1
      else:
            return num*fact(num-1)
print("enter a number :")
n=int(input())
print("factorial of num ",n, "is :",fact(n))