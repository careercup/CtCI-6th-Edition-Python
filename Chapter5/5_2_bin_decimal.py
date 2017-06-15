

def bin_rep(freq_num):
	bin_num = bin(int(str(freq_num)[2:]))[2:]
	if len(bit_num) > 32:
		return False
	return '0.' + bin_num


bin_rep(0.1738)
