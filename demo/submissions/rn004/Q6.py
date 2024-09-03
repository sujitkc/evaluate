#ndiamond


def ndiamond(n):

	for i in range(1,n+1,2):#first half of diamond

		print(" "*((n-i)//2),end="")

		count=0

		for j in range(1,(i+1)//2+1):
			print(j,end="")
			count+=1

		for k in range(count-1,0,-1):
			print(k,end="")


		print()


	for i in range(n-2,0,-2):#second half

		print(" "*((n-i)//2),end="")
		count=0

		for j in range(1,(i+1)//2+1):
			print(j,end="")
			count+=1

		for k in range(count-1,0,-1):
			print(k,end="")

		print()







ndiamond(19)