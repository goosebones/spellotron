"""
author: Gunther Kroth   gdk6217@rit.edu
file: adjacent.py
assignment: CS1 Project
purpose: check if a misspelled word was an adjacent key press
"""


# required modules
import word_check
import string_modify


def adjacent_key_press(word):
    """ trys to correct a word by adjacent key presses
        for each letter in the word, each adjacent key is tried
        returns boolean, word
        if word could be corrected, return True
        :param word: word to analyze
    """
    origional_word = word
    letter_idx = 0
    # each letter is checked
    for ch in word:
        if ch.isalpha() == False:
            letter_idx += 1
        elif ch.isupper() == True:
            letter_idx += 1
        else:
            # every adjacent key is checked
            adjacent_keys = word_check.ADJACENT_KEYS[ch]
            for key in adjacent_keys:
                word = swap_letter(word, key, letter_idx)
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


def swap_letter(word, letter, idx):
    """ swaps in a letter into a word at an index
        uses a list method
        :param word: word to modify
        :param letter: letter to swap into word
        :param idx: index to swap letter in at
    """
    letter_list = []
    new_word = ""
    for ch in word:
        letter_list.append(ch)
    letter_list[idx] = letter
    for element in letter_list:
        new_word += element
    return new_word
