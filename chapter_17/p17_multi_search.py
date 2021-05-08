# trie solution
# third optimal solution in ctci
# o(kt+bk)
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True

    def check_existence(self, word):
        # checks if the prefixes exist on a path,
        # if they do, then return the location in the word
        res = []
        node = self.root
        for i, letter in enumerate(word):
            if letter in node.children.keys():
                node = node.children[letter]
                if node.is_word:
                    res.append(word[0 : i + 1])
            else:
                break
        return res


def multisearch(text, search_terms):
    t = Trie()

    # insert t's in trie
    for word in search_terms:
        t.insert(word)
    # a dict with t's element as keys, and all the possible indices
    # where they are discovered in string
    res = collections.defaultdict(list)
    # start matching the sentence now
    n = len(text)
    for i in range(n):
        discovered_words = t.check_existence(text[i:])
        for word in discovered_words:
            # the discovered word, starts at i
            res[word].append(i)
    return dict(res)


def test_multisearch():
    small_words = ["i", "is", "pp", "ms"]
    expected = {"i": [1, 4, 7, 10], "is": [1, 4], "pp": [8]}
    assert multisearch("mississippi", small_words) == expected
