

def mattrans(l):

	n=[]

	for i in range(len(l[0])):

		m=[]

		for j in range(len(l)):

			m.append(l[j][i])

		n.append(m)




	return n

if __name__=="__main__":
    print(mattrans([[1,2,9,4],[3,4,6,10]]))