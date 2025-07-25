# print("Enter a number ")
# n =int(input())

# b=1
# a=0
# i=0
# while i<n :
#   c=a+b
#   a=b
#   b=c

#   i=i+1
#   print(c)
a=0

def Fibonacci(n):
  

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		
		
		print("called \n",a)
		return Fibonacci(n-1) + Fibonacci(n-2)


# Driver Program
print(Fibonacci(9))
