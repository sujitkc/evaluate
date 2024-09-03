#ndiamond


def ndiamond():

	for i in range(1,6,2):#first half

		print(" "*((5-i)//2),end="")

		count=0

		for j in range(1,(i+1)//2+1):
			print(j,end="")
			count+=1

		for k in range(count-1,0,-1):
			print(k,end="")


		print()


	for i in range(3,0,-2):#second half

		print(" "*((5-i)//2),end="")
		count=0

		for j in range(1,(i+1)//2+1):
			print(j,end="")
			count+=1

		for k in range(count-1,0,-1):
			print(k,end="")

		print()







#ndiamond()