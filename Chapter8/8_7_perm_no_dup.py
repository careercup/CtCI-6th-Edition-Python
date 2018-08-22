
import unittest


def UniqPerm(s):
	""" take a string as an input and returns a list of all 
		permutations of that string """

	if len(set(s)) != len(s):
		raise TypeError('this function only accepts strings with uniqe characters')
	perms = [s]

	if len(s) <= 1:
		return perms

	for pos, i in enumerate(s):

		rest_of_string = s[:pos] + s[pos+1:]

		sub_perms = UniqPerm(rest_of_string)

		for sub in sub_perms:
			if i+sub not in perms:
				perms.append(i+sub)

	return perms


class TestPerm(unittest.TestCase):
	def test_no_uniq(self):
		self.assertEqual(sorted(UniqPerm('abc')), sorted(['abc',
															'acb',
															'bca',
															'bac',
															'cab',
															'cba']))
	def test_uniq_perm(self):
		with self.assertRaises(TypeError):
			UniqPerm('nooot unique')
if __name__ == '__main__':

	unittest.main()
