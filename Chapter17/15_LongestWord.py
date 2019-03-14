import unittest

def longest_composite_word(list):
    dict = {}

    for word in list:
        dict[word] = True

    for original_word in sorted(list, key=len, reverse=True):
        if contains_subwords(original_word, True, dict):
            return original_word

    return 

def contains_subwords(word, is_original_word, dict):
    if (word in dict) and (not is_original_word):
        return dict[word]

    for i in xrange(1, len(word)):
        left = word[0:i]
        right = word[i:]

        if (left in dict) and (dict[left] == True) and (contains_subwords(right, False, dict)):
            return True

    dict[word] = False
    return False

class Test(unittest.TestCase):
    def test_lcw(self):
        word_list = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
        result = longest_composite_word(word_list)
        self.assertEqual(result, 'dogwalker')

    def test_lcw_returns_none_for_no_match(self):
        word_list = ['cat', 'banana', 'dog']
        result = longest_composite_word(word_list)
        self.assertEqual(result, None)

    def test_lcw_checks_alphabetically(self):
        word_list = ['cat', 'banana', 'dog', 'nana', 'catbanana', 'walk', 'walker', 'dogwalker']
        result = longest_composite_word(word_list)
        self.assertEqual(result, 'catbanana')

if __name__ == "__main__":
    unittest.main()

