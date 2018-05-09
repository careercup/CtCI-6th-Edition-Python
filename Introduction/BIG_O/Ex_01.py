class Ex_01:
	def sum_int(n):
		if n <=0:
			return 0
		else:
			return n + Ex_01.sum_int(n-1)

print(Ex_01.sum_int(5))