#trie solution
#third optimal solution in ctci
#o(kt+bk)
import collections
class trienode:
    def __init__(self):
        self.children=collections.defaultdict(trienode)
        self.is_word = False

class trie:
    def __init__(self):
        self.root = trienode()
    def insert(self,word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True
    def check_existence(self,word):
        #checks if the prefixes exist on a path,
        #if they do, then return the location in the word
        res = []
        node = self.root
        for i,letter in enumerate(word):
            if letter in node.children.keys():
                node = node.children[letter]
                if node.is_word:
                    res.append(word[0:i+1])
            else:
                break
        return res

small_words = ['i','is','pp','ms']
s = 'mississippi'
t = trie()

#insert t's in trie
for word in small_words:
    t.insert(word)
#a dict with t's element as keys, and all the possible indices where they are discovered in string
res = collections.defaultdict(list)
#start matching the sentence now
n = len(s)
for i in range(n):
    discovered_words = t.check_existence(s[i:])
    for word in discovered_words:
        #the discovered word, starts at i
        res[word].append(i)
print(res)