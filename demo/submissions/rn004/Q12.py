

def check_mult(m1,m2):

	if len(m1)==len(m2[0]) and len(m1[0])==len(m2):

		return True

	else:
		return False


def matmul(m1,m2):

	if not (check_mult(m1,m2)):

		return "Matrices cannot be multiplied"

	else:

		n=[]#final matrix

		for i in range(len(m1)):
			l=[]#each row of the resultant matrix

			for j in range(len(m2[0])):

				s=0#sum of products . Equate to 0 after finishing 1 col or row

				for k in range(len(m1[0])):

					#print("m1[i][j]:",m1[i][j])
					#print("m2[k][j]:",m2[k][j])

					s+=m1[i][k] * m2[k][j]

					#print("s=",s)


				l.append(s)



			n.append(l)

		return n



if __name__=="__main__":
    a=matmul([[1,2,3,3],[4,5,6,9]],[[7,10],[8,11],[9,12]])

    print(a)






