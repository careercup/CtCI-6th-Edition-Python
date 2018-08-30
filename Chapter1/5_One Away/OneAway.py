import unittest

def one_away(a, b):

	# Case 1 : The two strings have the same length.
	if(len(a) == len(b)):

		# Case 1.1 : No edits away, i.e the strings are identical.
		if(a==b):
			return True

		# Case 1.2 : The string is just 1 edit away,
		#            which in this case would just be
		#            one character replaced.
		elif(len(set(a)&set(b)) == len(a)-1):
			return True

		# Case 1.3 : The string is not 1 or 0 edits away,
		#            in which case the function should return
		#            False.
		else:
		    return False
	    
	
	# Case 2 : The two strings are of different lengths
	elif(abs(len(a)-len(b)) == 1):

		smaller_strlen = min(len(a), len(b))
		
		# Case 2.1 : The only scenario where this should return True
		#            is when the strings are 1 removal or insertion 
		#            away. So, the length of the intersection of the
		#            2 strings in sets should be equal to the length
		#            of the smaller string.
		if(len(set(a)&set(b)) == smaller_strlen):
			return True

		# Case 2.2 : No 1 or 0 edits away.
		else:
		    return False
	    

	# Case 3 : The two strings are not 1 or 0 edits away
	else:
	    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()	
