"""
author: Gunther Kroth   gdk6217@rit.edu
file: word_check.py
assignment: CS1 Project
purpose: spell check a word
"""


# required modules
from dataclasses import dataclass
import adjacent
import missed
import extra
import string_modify


# golbal variables ------------------------------------------------------------
LEGAL_WORD_FILE = "american-english.txt"
KEY_ADJACENCY_FILE = "keyboard-letters.txt"
ALPHABET = tuple(chr(code) for code in range(ord("a"), ord("z") +1))
LEGAL_WORDS = dict()
ADJACENT_KEYS = dict()

# legal word dictionary
def legal_words_maker(word_file):
    """ creates dictionary of legal_words
        key and value are identical
        dictionary keys are used throughout
        :param word_file: file containing dictionary words
        preconditions:
            word_file has one word per line
        postconditions:
            LEGAL_WORDS dict is populated
    """
    f = open(word_file)
    for line in f:
        line = line.strip()
        LEGAL_WORDS[line] = line
        
legal_words_maker(LEGAL_WORD_FILE)

# adjacent keys
def adjacent_letter_maker(letter_file):
    """ creates dictionary of adjacent keys
        each letter is a key
        list of every key adjacent to the letter is value
        :param letter_file: file with adjacent keys
        preconditions:
            letter_file has one set of keys per line
        postconditions:
            ADJACENT_KEYS is populated
    """
    f = open(letter_file)
    for line in f:
        key = line[0]
        value = line.split()
        ADJACENT_KEYS[key] = value
        
adjacent_letter_maker(KEY_ADJACENCY_FILE)

# words that have been checked 
printed_words = []
# key = incorrect word, value = correct version
fixed_words = dict()
# words that were unable to be fixed
unknown_words = []
# number of words analyzed
word_count = 0


# word dataclass --------------------------------------------------------------
@dataclass
class Word:
    """ dataclass for a word
        word = read word
        front = front punctuation
        back = back punctuation
        capital = first letter capital
    """
    __slots__ = "word", "front", "back", "capital"
    word: str
    front: str
    back: str
    capital: bool

def word_maker(word):
    """ returns instance of Word dataclass
        read word is word
        punctuation is empty
        capital is False
        :param word: word to use to create instance
    """
    return Word(word, "", "", False)

# word analyze ----------------------------------------------------------------
def line_check(line):
    """ analyzes lines that are read
        analyzes each word in the line using word_check
        :param line: line of words to check
        preconditions:
            line is list of words
    """
    global word_count
    for word in line:
        word_check(word)
        word_count += 1

def word_check(word):
    """ spell checks a word
        accounts for symbols, decimals, punctuation, capitals
        used 3 methods to spell check an incorrect word
        return None is used as an exit method
        :param word: word to analyze
    """
    word = word_maker(word)
    
    # 2. decimal digits
    for ch in word.word:
        if ch.isdigit() == True:
            printed_words.append(word.word)
            return None
        
    # 3. strip punctuation
    word.word, word.front, word.back = string_modify.punctuation_strip(word.word)
    # word is all punctuation
    if len(word.word) == 0:
        punct_word = word.front + word.word + word.back
        printed_words.append(punct_word)
        return None
    
    # 4. spell check
    if word.word in LEGAL_WORDS:
        printed_words.append(word.front + word.word + word.back)
        return None
    
    # 5. upper case
    if word.word[0].isupper() == True:
        word.capital = True
    if word.capital == True:
        first_letter = word.word[0]
        word.word = string_modify.lower_case(word.word)
        if word.word in LEGAL_WORDS:
            word.word = first_letter + word.word[1:]
            printed_words.append(word.front + word.word + word.back)
            return None
        
    # 6. check using methods
    
    # adjacent key press
    adj_bool, fixed_word = adjacent.adjacent_key_press(word.word)
    if adj_bool == True:
        new = word.front + fixed_word + word.back
        old = word.front + word.word + word.back
        # 7. case is restored
        if word.capital == True:
            new = word.front + string_modify.upper_case(fixed_word) + word.back
            old = word.front + string_modify.upper_case(word.word) + word.back
        printed_words.append(new)
        fixed_words[old] = new
        return None

    # missed key press
    miss_bool, fixed_word = missed.missing_key_press(word.word)
    if miss_bool == True:
        new = word.front + fixed_word + word.back
        old = word.front + word.word + word.back
        # 7. case is restored
        if word.capital == True:
            new = word.front + string_modify.upper_case(fixed_word) + word.back
            old = word.front + string_modify.upper_case(word.word) + word.back
        printed_words.append(new)
        fixed_words[old] = new
        return None

    # extra key press
    extra_bool, fixed_word = extra.extra_key_press(word.word)
    if extra_bool == True:
        new = word.front + fixed_word + word.back
        old = word.front + word.word + word.back
        # 7. case is restored
        if word.capital == True:
            new = word.front + string_modify.upper_case(fixed_word) + word.back
            old = word.front + string_modify.upper_case(word.word) + word.back
        printed_words.append(new)
        fixed_words[old] = new
        return None

    # could not be fixed
    unknown_word = word.front + word.word + word.back
    # 7. case is restored
    if word.capital == True:
        unknown_word = word.front + string_modify.upper_case(word.word) + word.back
    printed_words.append(unknown_word)
    unknown_words.append(unknown_word)
    return None
    

    
    

