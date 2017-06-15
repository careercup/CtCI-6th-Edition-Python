
""" when the break and count reset occurs, need to reset back to the previous 1 starting
	point, in order to hit the next window
	

	other problem, its returning 10 which is too high, counting is flawed somewhere

	solution, if a break is hit, pop up to the first zeros and try again"""


def flip_bit(int_or_bi_string):
	if type(int_or_bi_string) == int:
		int_or_bi_string = bin(int_or_bi_string)[2:]
	max_count = 0
	current_len = 0
	current_0s = 0
	for i in int_or_bi_string:
		if i == '1':
			current_len += 1
		elif (i=='0') and (current_0s == 0):
			current_0s += 1
			current_len += 1
		elif (i=='0') and (current_0s == 1):
			current_0s = 0
			if current_len > max_count:
				max_count = current_len
			continue
	if current_len > max_count:
		max_count = current_len
	return max_count

flip_bit(1775)

in_bin='1010011010'