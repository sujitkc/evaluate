

def diamond(n):
	for i in range(1,n+1,2):
		print(" "*((n-i)//2),end="")

		print("*"*i)

	for i in range(n-2,0,-2):
		print(" "*((n-i)//2),end="")

		print("*"*i)

#diamond(9)