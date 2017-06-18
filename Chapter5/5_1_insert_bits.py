


def insert_bits(major, minor, start, end):
	temp = str(major)[-(end+1):-(start)]
	new = bin(int(minor,2))
	new_major = major[:-(end+1)] + new[2:] + major[-start:]
	return new_major

test_a = insert_bits('00000000000000000', '111', 2,5) 