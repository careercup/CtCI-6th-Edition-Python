
x = '011011'
y=  '001011'

def flip_counter(bin_A,bin_B):
	if type(bin_A) == int:
		x = list(bin(bin_A))[:2]
	else:
		x = list(bin_A)
	if type(bin_B) == int:
		y = list(bin(bin_B))[:2]	
	else:
		y = list(bin_B)
	flip_count = 0
	while len(x) != 0:
		if x.pop(-1) != y.pop(-1):
			flip_count +=1
		else:
			continue
	return flip_count