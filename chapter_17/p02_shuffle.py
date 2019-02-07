import random
import unittest


def random_number_generator(lower, higher):
    return lower + int(random.random() * (higher - lower + 1))


def shuffle_list_recursively(cards, current_index):
    if current_index == 0:
        return cards

    shuffle_list_recursively(cards, current_index - 1)
    random_index = random_number_generator(0, current_index)

    temp = cards[random_index]
    cards[random_index] = cards[current_index]
    cards[current_index] = temp

    return cards


def shuffle_list_iteratively(cards):
    for i in range(len(cards) - 1):
        random_index = random_number_generator(0, i)
        temp = cards[random_index]
        cards[random_index] = cards[i]
        cards[i] = temp

    return cards


class TestShuffles(unittest.TestCase):
    cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_shuffle_list_recursively(self):
        result = shuffle_list_recursively(self.cards, len(self.cards) - 1)
        self.assertEqual(len(result), len(self.cards))
        self.assertEqual(sum(result), sum(range(0, len(self.cards))))

    def test_shuffle_list_iteratively(self):
        result = shuffle_list_iteratively(self.cards)
        self.assertEqual(len(result), len(self.cards))
        self.assertEqual(sum(result), sum(range(0, len(self.cards))))


if __name__ == "__main__":
    unittest.main()
