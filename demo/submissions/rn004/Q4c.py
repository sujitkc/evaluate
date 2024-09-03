def diamond(n,c):
	for i in range(1,n+1,2):
		print(" "*((n-i)//2),end="")

		print(c*i)

	for i in range(n-2,0,-2):
		print(" "*((n-i)//2),end="")

		print(c*i)

#diamond(3,'7')