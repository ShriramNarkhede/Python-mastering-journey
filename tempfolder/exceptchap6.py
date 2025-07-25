try:
    a=int(input("enter a :"))
    b=int(input("enter b :"))
    c=a/b
except ArithmeticError:
    print("exception occurs000000")
except ValueError:
    print("exception wrong value")
else:
    print("result:",c)