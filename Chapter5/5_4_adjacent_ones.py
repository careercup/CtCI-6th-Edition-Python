

def count_ones(integer):
	count = 0
	for i in bin(integer):
		if i == '1':
			count += 1
	return count

def check_adj(integer, query_ones, direction):
	if coutn_ones(integer) == query_ones:
		return integer
	elif direction == 'lower':
		check_adj(integer-1, query_ones, direction)
	elif direction == 'higher':
		check_adj(integer+1, query_ones, direction)

def adj_same_ones(number):
	num_one_count = count_ones(number)
	higher_neighbour = check_adj(number+1, number_one_count, 'higher')
	lower_neighbour = check_adj(number-1, number_one_count, 'lower')