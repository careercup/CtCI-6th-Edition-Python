

def Permutations(s):
	""" take a string as an input and returns a list of all 
		permutations of that string """

	perms = [s]

	if len(s) <s= 1:
		return perms

	for pos, i in enumerate(s):

		rest_of_string = s[:pos] + s[pos+1:]

		sub_perms = Permutations(rest_of_string)

		for sub in sub_perms:
			if i+sub not in perms:
				perms.append(i+sub)

	return perms





if __name__ == '__main__':


	s = 'test16'

	test_out = Permutations(s)

	for x in test_out:
		print(x)

	print(len(test_out))