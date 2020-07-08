"""
author: Gunther Kroth   gdk6217@rit.edu
file: missed.py
assignment: CS1 Project
purpose: check if a misspelled word was a missed key press
"""


# required modlues
import word_check
import string_modify


def missing_key_press(word):
    """ trys to correct a word by inserting letters
        for each letter in the word, every letter is inserted
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
            # every alphabet letter is inserted at each spot
            for letter in word_check.ALPHABET:
                word = add_letter(word, letter, letter_idx)
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

def add_letter(word, letter, idx):
    """ inserts a letter into a word at an index
        uses a list method
        :param word: word to modify
        :param letter: letter to insert into word
        :param idx: index to insert letter at
    """
    letter_list = []
    new_word = ""
    for ch in word:
        letter_list.append(ch)
    letter_list.insert(idx + 1, letter)
    for element in letter_list:
        new_word += element
    return new_word
                
