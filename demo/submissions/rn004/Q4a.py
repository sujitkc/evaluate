#Write a function diamond() that prints a diamond of height 5.

def diamond():
	for i in range(1,6,2):#first half
		print(" "*((5-i)//2),end="")

		print("*"*i)

	for i in range(3,0,-2):#second half
		print(" "*((5-i)//2),end="")

		print("*"*i)

#diamond()