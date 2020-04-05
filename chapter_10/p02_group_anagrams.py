from collections import defaultdict


def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        anagrams[sorted_word].append(word)

    sorted_words = []
    for similar_words in anagrams.values():
        sorted_words.extend(similar_words)
    return sorted_words


def test_group_anagrams():
    words = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]
    expected_sort = [
        "abed",
        "bead",
        "bade",
        "later",
        "alert",
        "alter",
        "altered",
        "alerted",
    ]
    assert group_anagrams(words) == expected_sort


def example():
    words = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]
    print(group_anagrams(words))


if __name__ == "__main__":
    example()
