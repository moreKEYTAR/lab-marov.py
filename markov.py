"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_text = open(file_path).read()
    return file_text


    # your code goes here

    return "Contents of your file as one long string"


def make_chains(text_string):
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
    words.append(None)

    chains = {}

    # for i, word in enumerate(words):
    #     if i < len(words) - 2:
    for i in range(len(words) - 2):
        ngram_key = (words[i], words[i + 1])

        if chains.get(ngram_key):  # Checks ngram_key exist in a Dict
            # word_paths_list = chains[ngram_key]
            # word_paths_list.append(words[i + 2])
            # chains[ngram_key] = word_paths_list
            # OR -
            chains[ngram_key].append(words[i + 2])

        else:
            # word_paths_list = []
            # word_paths_list.append(words[i + 2])
            # chains[ngram_key] = word_paths_list
            chains[ngram_key] = [words[i + 2]]

            # i += 1

        # elif i < len(words) - 1:
        #     ngram_key = (words[i], words[i + 1])
        #     if not chains.get(ngram_key):
        #         # ngram_key = words[i], words[i+1]
        #         chains[ngram_key] = None

    #print chains
    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(chains.keys())
    words = list(key)

    while True:
        # for ngram_keys in chains.keys():
        next_word = choice(chains[key])
        if next_word is None:
            break
        words.append(next_word)
        key = (words[-2], words[-1])
       
    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
