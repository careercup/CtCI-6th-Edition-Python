def preprocess(book):
    ht = {} # hashtable
    for word in book.split():
        word = word.lower()
        if word == '':
            continue
        elif word not in ht:
            ht[word] = 1
        else:
            ht[word] += 1
    return ht

def get_frequency(word, ht):
    if ht == {} or word == None:
        return 0
    elif word.lower() not in ht:
        return 0
    else:
        return ht[word.lower()]

book = 'Once upon a time there was this book. \
        This is a sentence. This is a much longer sentence. \
        This is a terribly short example. But you get the idea. \
        You should see the word this 6 times in this example text.'

ht = preprocess(book)

word = 'this'

print('The word "' + word + '" appears ' + str(get_frequency(word, ht)) + ' times.')
