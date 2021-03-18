"""
Note:
Three things are important for this solution
[1] Problem is to 'reach' target word, from a source word. This is modelled as a graph. THe constraint b/w edge is that
a word has to be one hop away from another.
[2] To check, one hop words from a given word, one method is to compare a candidate word with all the words in the dict.
[2.1] This yields o(w^2*l) complexity. [and space]
[2.2] an alternate way is to estimate the state of the bfs at the runtime [which this code does]
[2.3] another alternate way is to consider the 'no of possible letters at each location of the word'. So, we can convert a dictionary to a hashset. Next, for a given word,
try to generate all the possible one hop words. Checking whether a given word exists in the dictionary, is a simple matter of lookup in the hashset which is o(1)

[3] Final optimization: This method relies on bfs through the graph. An alternate way, is to perform a bidirectional bfs through the graph, till the two frontiers collide.
This has not been implemented in this code.
"""
import collections
def word_transformer(source, target, words):
    # state function
    # takes a word, gives the other words one hop away
    def state(word1):
        res = []
        for word2 in words:
            # check whether word1 and word2 are one hop away
            if word2 != word1 and len(word2) == len(word1):
                n_unequal_chars = 0
                for i in range(len(word2)):
                    if word1[i] != word2[i]:
                        n_unequal_chars += 1
                if n_unequal_chars == 1:
                    res.append(word2)
        return res
    #function to reconstruct the path from parent pointers after bfs
    def reconstruct_path(parents,target):
        res = []
        res.append(target)
        temp =target
        while temp:
            temp= parents[temp]
            res.append(temp)
        return res[::-1] #list needs to be reversed since we need the path from source to target. parent pointers are in opposite directions by default

    # naive bfs loop
    import collections
    q = collections.deque()
    visited = set()
    q.append(source)
    level = 0
    #a dictionary to keep a track of the parent pointers
    parents = collections.defaultdict(str)
    parents[source]=None

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == target:
                path = reconstruct_path(parents,target)
                return path,level
            visited.add(word)
            # get neighbouring words
            neighs = state(word)
            for neigh in neighs:
                if neigh not in visited:
                    parents[neigh]= word
                    q.append(neigh)
        level += 1
    return -1

#test case 1
source = "bit"
target = "dog"
dictionary = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(word_transformer(source,target,dictionary))


#test case 2 (from ctci)
source = "damp"
target = "like"
dictionary = ["damp","lime","limp","lamp","like"]
print(word_transformer(source,target,dictionary))
