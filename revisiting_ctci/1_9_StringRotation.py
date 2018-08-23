import unittest



def IsRotation(a,b):
	""" take strings a and b as an input and see if they are rotations
		of one another, returns boolean """
	rotation = 0
	rotate_max = len(a)

	while rotation < rotate_max:
		rotation += 1

		if a == b:
			return True

		a = a[-1] + a[:-1]

	return False


class TestRotate(unittest.TestCase):
	def test_IsRotation(self):
		self.assertTrue(IsRotation('test','ttes'))
		self.assertTrue(IsRotation('test','estt'))

		self.assertFalse(IsRotation('test','sett'))
		self.assertFalse(IsRotation('test','nottest'))

if __name__ == '__main__':


	unittest.main()