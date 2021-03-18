import collections
#make a trie node
class trienode(object):
    def __init__(self):
        self.children = collections.defaultdict(trienode)
        self.is_word = False
#define a trie
class trie(object):
    def __init__(self):
        self.root = trienode()
    #method to insert in the trie
    def insert(self,word):
        node = self.root
        for letter in word:
            node= node.children[letter]
        node.is_word = True
    #checks the word [i,j] matches in trie
    def is_match(self,word):
        node = self.root
        for letter in word:
            if letter in node.children.keys():
                node = node.children[letter]
            else:
                return False
        if node.is_word:
            return True
        return False
    #penalty function for te dp [similar to mit's 6.006 text justification]
    def penalty(self,word):
        if self.is_match(word)==True:
            return 0
        return len(word)
word_dict = ["looked","just","like","her","brother"]
sentence = "jessjustlookedliketimherbrother"
#insert words in trie
t = trie()
for word in word_dict:
    t.insert(word)

n = len(sentence)
dp = [0]*(n+1)
for i in reversed(range(n)):
    choices = [float('inf')]
    for j in range(i+1,n+1):
        curr_penalty = t.penalty(sentence[i:j])+ dp[j]
        choices.append(curr_penalty)
    dp[i]=min(choices)
print(dp[0])
