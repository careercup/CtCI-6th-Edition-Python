

def bit_swap(bit_string):
	eve_bits = list(bit_string)[0::2]
	odd_bits = list(bit_string)[1::2]
	out = []
	for i in zip(odd_bits,even_bits):
		out.extend(list(i))
	return out