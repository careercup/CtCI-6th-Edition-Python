import string

def get_frequency(book, word):
    if book == None or word == None:
        return 0
    word = word.lower()
    count = 0
    for book_word in book.split():
        # make lowercase, remove punctuation
        book_word = book_word.lower().translate(None, string.punctuation)
        if book_word == word:
            count += 1
    return count

book = 'Once upon a time there was this book. \
        This is a sentence. This is a much longer sentence. \
        This book is terribly short. But you get the idea. \
        You should see the word this 6 times in this example text.'

word = 'book'

print('The word "' + word + '" appears ' + str(get_frequency(book, word)) + ' times.')
