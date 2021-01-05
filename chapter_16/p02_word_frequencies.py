import string


def preprocess(book):
    word_counts = {}
    for word in book.split():
        word = word.lower()
        word = word.translate(str.maketrans("", "", string.punctuation))
        if not word:
            continue

        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts


def get_frequency_repetitive(book, word):
    word_counts = preprocess(book)
    return word_counts.get(word.lower(), 0)


def get_frequency_single_query(book, word):
    if book is None or word is None:
        return 0
    word = word.lower()
    count = 0
    for book_word in book.split():
        # make lowercase, remove punctuation
        book_word = book_word.lower()
        book_word = book_word.translate(str.maketrans("", "", string.punctuation))
        if book_word == word:
            count += 1
    return count


def example():
    book = """Once upon a time there was this book.
            This is a sentence. This is a much longer sentence.
            This book is terribly short. But you get the idea.
            You should see the word this 6 times in this example text.
            """
    word = "book"

    count = get_frequency_repetitive(book, word)
    print(f'The word "{word}" appears {count} times.')

    count = get_frequency_single_query(book, word)
    print(f'The word "{word}" appears {count} times.')


if __name__ == "__main__":
    pass
