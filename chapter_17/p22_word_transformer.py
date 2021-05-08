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

    # function to reconstruct the path from parent pointers after bfs
    def reconstruct_path(parents, target):
        res = [target]
        temp = target
        while temp:
            temp = parents[temp]
            res.append(temp)
        # list needs to be reversed since we need the path from source to target.
        # parent pointers are in opposite directions by default
        return res[::-1]

    # naive bfs loop

    q = collections.deque()
    visited = set()
    q.append(source)
    level = 0
    # a dictionary to keep a track of the parent pointers
    parents = collections.defaultdict(str)
    parents[source] = None

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == target:
                path = reconstruct_path(parents, target)
                return path[1:]
            visited.add(word)
            # get neighbouring words
            neighs = state(word)
            for neigh in neighs:
                if neigh not in visited:
                    parents[neigh] = word
                    q.append(neigh)
        level += 1
    return -1


def test_word_transformer():
    source = "bit"
    target = "dog"
    dictionary = ["but", "put", "big", "pot", "pog", "dog", "lot"]
    expected = ["bit", "but", "put", "pot", "pog", "dog"]
    assert word_transformer(source, target, dictionary) == expected

    source = "damp"
    target = "like"
    dictionary = ["damp", "lime", "limp", "lamp", "like"]
    expected = ["damp", "lamp", "limp", "lime", "like"]
    assert word_transformer(source, target, dictionary) == expected
