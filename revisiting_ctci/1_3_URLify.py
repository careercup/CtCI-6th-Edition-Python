import unittest



def URL(s):
	""" take an input string and replace spaces with %20"""
	return s.replace(" ", "%20")


class TestURL(unittest.TestCase):
	def test_URLfunc(self):
		self.assertEqual(URL("this is the string"), "this%20is%20the%20string")


if __name__ == '__main__':
	unittest.main()