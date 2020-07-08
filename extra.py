"""
author: Gunther Kroth   gdk6217@rit.edu
file: extra.py
assignment: extra.py
purpose: check if a misspelled word was an extra key press
"""


# required modules
import word_check
import string_modify


def extra_key_press(word):
    """ trys to correct a word by removing key presses
        for each letter in the word, the letter is removed
        returns boolean, word
        if word count be corrected, return True
        :param word: word to analyze
    """
    origional_word = word
    letter_idx = 0
    # each letter is checked
    for ch in word:
        # delete letter 
        word = delete_letter(word, letter_idx)
        # lowercase check
        if word in word_check.LEGAL_WORDS:
            return True, word
        # uppercase version check
        word = string_modify.upper_case(word)
        if word in word_check.LEGAL_WORDS:
            return True, word
        word = origional_word
        letter_idx += 1
        
    return False, origional_word

def delete_letter(word, idx):
    """ deletes a letter from a word an an index
        uses a list method
        :param word: word to modify
        :param idx: index to delete at
    """
    letter_list = []
    new_word = ""
    for ch in word:
        letter_list.append(ch)
    del letter_list[idx]
    for element in letter_list:
        new_word += element
    return new_word
