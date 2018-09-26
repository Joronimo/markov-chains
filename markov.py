"""Generate Markov text from text files."""

from random import choice

import sys

def open_and_read_file(file_path_1, file_path_2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path_1, 'r') as file1:
        data = file1.read()
    with open(file_path_2, 'r') as file2:
        data += ' ' + file2.read()

 
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
    

    for i in range(len(word) - n):
        n_gram = tuple(word[i:i+n])
        next_word = word[i + n]
        chains[n_gram] = chains.get(n_gram, []) + [next_word]

    return chains


def make_text(chains):
    """Return text from chains."""

    upper_words = []

    
    for word in list(chains):
        if word[0][0].isupper():
            upper_words.append(word)

    key = choice(upper_words)
            
    words = list(key)

    end_punc = ['.', '?', '!']

    while key in chains and words[-1][-1] not in end_punc:
        value = choice(chains[key])
        words.append(value)
        key = (key[1:] + (value,))

    return " ".join(words)


# input_path = "green-eggs.txt"[-1]

# # Open the file and turn it into one long string
# input_text = 
input_text = open_and_read_file(sys.argv[1], sys.argv[2])
n = int(sys.argv[3])
loop_num = int(sys.argv[4])

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
