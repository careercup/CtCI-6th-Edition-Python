
""" when the break and count reset occurs, need to reset back to the previous 1 starting
	point, in order to hit the next window
	

	other problem, its returning 10 which is too high, counting is flawed somewhere

	solution, if a break is hit, pop up to the first zeros and try again"""


def flip_bit(int_or_bi_string):
	if type(int_or_bi_string) == int:
		int_or_bi_string = bin(int_or_bi_string)[2:]
	list_of_types = []
	counter = 1
	current = int_or_bi_string[0]
	for z, i in enumerate(int_or_bi_string[1:]):
		if i == current:
			counter += 1
			if z == (len(int_or_bi_string[1:])-1):
				list_of_types.append((current, counter))
		else:
			list_of_types.append((current, counter))
			current = i 
			counter = 1
			if z == (len(int_or_bi_string[:1])-1):
				list_of_types.append((current, counter))
	len_max = 0
	for x in range(0,len(list_of_types)):
		if (list_of_types[x][0] == '0' ) and (list_of_types[x][1] == 1):
			if(x == (len(list_of_types)-1)):
				current = (list_of_types[x-1][1])+(list_of_types[x][1])
			else:
				current = (list_of_types[x-1][1])+(list_of_types[x][1])+(list_of_types[x+1][1])
			if current > len_max:
				len_max = current
	return len_max

flip_bit('0001110111')



