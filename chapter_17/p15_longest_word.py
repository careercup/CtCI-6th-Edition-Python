def longest_composite_word(word_list):
    mapping = {}

    for word in word_list:
        mapping[word] = True

    for original_word in sorted(word_list, key=len, reverse=True):
        if contains_subwords(original_word, True, mapping):
            return original_word

    return None


def contains_subwords(word, is_original_word, mapping):
    if (word in mapping) and (not is_original_word):
        return mapping[word]

    for i in range(1, len(word)):
        left = word[0:i]
        right = word[i:]

        if (
            (left in mapping)
            and (mapping[left] is True)
            and (contains_subwords(right, False, mapping))
        ):
            return True

    mapping[word] = False
    return False


def test_lcw():
    word_list = ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
    result = longest_composite_word(word_list)
    assert result == "dogwalker"


def test_lcw_returns_none_for_no_match():
    word_list = ["cat", "banana", "dog"]
    result = longest_composite_word(word_list)
    assert result is None


def test_lcw_checks_alphabetically():
    word_list = [
        "cat",
        "banana",
        "dog",
        "nana",
        "catbanana",
        "walk",
        "walker",
        "dogwalker",
    ]
    result = longest_composite_word(word_list)
    assert result == "catbanana"
