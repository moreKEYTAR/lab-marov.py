"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_text = open(file_path).read()
    return file_text


    # your code goes here

    return "Contents of your file as one long string"


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()  # now we have a list of words
    words.append(None) # helps for knowing the end of the text

    chains = {}

    # for i, word in enumerate(words):
    #     if i < len(words) - 2:
    for i in range(len(words) - n):

        # make an ngram key
        if n > 0 and n < len(words):
            c = n  # counter
            ngram_key = ()
            while c > 0:
                next_word = tuple((words[i + (n - c)], ))
                ngram_key = ngram_key + next_word
                c -= 1 

        # OLD CODE FOR BIGRAM (before n implementation)
        # ngram_key = (words[i], words[i + 1])

        # Checks ngram_key exist in the dict, then add a value to the value list
        if chains.get(ngram_key):  
            # word_paths_list = chains[ngram_key]
            # word_paths_list.append(words[i + 2])
            # chains[ngram_key] = word_paths_list
            # OR -
            chains[ngram_key].append(words[i + n])

        # If the ngram_key doesn't already exist, start a list with a value
        else:
            # word_paths_list = []
            # word_paths_list.append(words[i + 2])
            # chains[ngram_key] = word_paths_list
            chains[ngram_key] = [words[i + n]]


    #print chains
    return chains


def make_text(chains, n):
    """Return text from chains."""

    key = choice(chains.keys())

    # Starting the output text with a list that begins with our first key
    words = list(key)

    while True:
        # for ngram_keys in chains.keys():
        next_word = choice(chains[key]) # <----
        if next_word is None:
            break
        words.append(next_word)

        # Makes the next key using the next word
        # key = (words[-n], words[-(n - 1)])
        c = 0  # counter
        key = () # making key empty again - tuple
        while c < n:
            next_word_in_key = tuple((words[-(n - c)], ))
            key = key + next_word_in_key
            c += 1 

    return " ".join(words)


n = 4 # this is the length of the ngram

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)
# print chains

# Produce random text
random_text = make_text(chains, n)

print random_text
