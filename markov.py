"""Generate Markov text from text files."""

from random import choice

import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')

 
    return data


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


    word = text_string.split()
    chains = {}
    

    for i in range(len(word) - 2):
        bigram = (word[i], word[i + 1])
        next_word = word[i + 2]
        chains[bigram] = chains.get(bigram, []) + [next_word]


    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains))

    words = [key[0], key[1]]

    #chains[key]

    while key in chains:
        value = choice(chains[key])
        words.append(value)
        key = (key[1], value)



    return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = 
input_text = open_and_read_file(sys.argv[1])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
