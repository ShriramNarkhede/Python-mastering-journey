
class abc:
    def __add(self,*varags):
        sum=0
        for ele in varags:
            sum=sum+ele
            print(sum)
    def sm(self,a,b,v):
        self.__add(a,b,v)

obj=abc()

obj.sm(2,4,5)
# obj.add(2,5,6,7,7,8,8,8,9,9)
# a= int(input("enter a number "))

# b= int(input("enter 2nd number "))

# c=7
# print("result is ",add(5,c))