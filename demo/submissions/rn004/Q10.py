# check for bracket correctness



def balanced_brackets(s):

	l=["0"]#so that I do not get list index out of range later

	d={")":"(","}":"{","]":"["}

	for i in s:
		if i=="(" or i=="{" or i=="[":
			l.append(i)
			continue

		if i in d and d[i]==l[-1]:

			l.pop()#removes last element

		elif i in d and d[i]!=l[-1]:

			break


	else:#runs when no break has occured
		return True


	return False


if __name__=="__main__":

    print(balanced_brackets("[]()"))
    print(balanced_brackets("[(])"))
    print(balanced_brackets(")("))


