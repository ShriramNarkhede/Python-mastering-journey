import sys
class Errror(Exception):
      def __init__(self ):
           print("div by zero or less is occurs ")
    

a=int(input("enter num :"))
try:
    if a<1:
        raise Errror
    div=80/a
    print("multt  is ", div)

except Errror:
    print("occurs")