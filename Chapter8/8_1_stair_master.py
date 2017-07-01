

def get_paths(stairs):
	paths = 0
	new_paths = [stairs - 1, stairs - 2, stairs - 3]
	for i in new_paths:
		if i > 3:
			next_level = get_paths(i) #recurse if more that 4
			paths += next_level
		elif i == 3:
			paths += 4
		elif i == 2:
			paths += 3
		elif i == 1:
			paths += 1
	return paths

if __name__ == '__main__':

	get_paths(4) #this one I did by hand
	get_paths(5) # seems pascal's triangly to me...
	get_paths(17) #i didn't count this out by hand...