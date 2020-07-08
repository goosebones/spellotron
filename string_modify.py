"""
author: Gunther Kroth   gdk6217@rit.edu
file: string_modify.py
assignment: CS1 Project
purpose: minipulate words that are being analyzed
"""


def punctuation_strip(word):
    """ strips punctuation from the front and back of a word
        returns a tuple of word, front, back
        :param word: word to strip punctuation from
    """
    front = ""
    back = ""
    # front strip
    while word[0].isalpha() == False:
        front += word[0]
        word = word[1:]
        if len(word) == 0:
            return word, front, back
    # back strip
    while word[-1].isalpha() == False:
        back += word[-1]
        word = word[:len(word)-1]
    # reverse back's order
    true_back = ""
    for ch in back:
        true_back = ch + true_back
        
    return word, front, true_back


def lower_case(word):
    """ convert first letter to lowercase
        uses a list method
        :param word: word to convert
    """
    letter_list = []
    new_word = ""
    for ch in word:
        letter_list.append(ch)
    first = letter_list[0]
    lower = first.lower()
    letter_list[0] = lower
    for element in letter_list:
        new_word += element
    return new_word


def upper_case(word):
    """ convert first letter to uppercase
        uses a list method
        :param word: word to convert
    """
    letter_list = []
    new_word = ""
    for ch in word:
        letter_list.append(ch)
    first = letter_list[0]
    cap = first.upper()
    letter_list[0] = cap
    for element in letter_list:
        new_word += element
    return new_word
