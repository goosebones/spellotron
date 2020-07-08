"""
author: Gunther Kroth   gdk6217@rit.edu
file: spellotron.py
assignment: CS1 Project
purpose: user input and command line arguments
"""


# required modules
import sys
import word_check


def input_handle():
    """ makes sense of user input in command line
        prints error message if incorect syntax is used
        prints information that goes with each mode
        return None is used as an exit method
    """
    # no mode given
    if len(sys.argv) < 2:
        print("Usage: python3.7 spellotron.py words/lines [filename]", file = sys.stderr)
        return None
    # word mode
    elif sys.argv[1] == "words":
        mode = "words"
    # line mode
    elif sys.argv[1] == "lines":
        mode = "lines"
        
    # determine text source
    if len(sys.argv) == 3:
        text_source = open(sys.argv[2])
        method = "file"
    elif len(sys.argv) == 2:
        text_source = sys.stdin
        method = "type"
    # final syntax catch
    else:
        print("Usage: python3.7 spellotron.py words/lines [filename]", file = sys.stderr)
        return None

    # file as input
    if method == "file":
        line = text_source.readline()
        while line != "":
            line = line.split()
            word_check.line_check(line)
            line = text_source.readline()
        text_source.close()
    # typing as input
    elif method == "type":
        line = text_source.readline()
        line = line.split()
        word_check.line_check(line)

    # line mode prints
    if mode == "lines":
        for word in word_check.printed_words:
            print(word, "", end = "")
        print()
    # word mode prints
    elif mode == "words":
        for key in word_check.fixed_words:
            old = key
            new = word_check.fixed_words[key]
            print(old, "->", new)

    # universal prints
    print()
    print(word_check.word_count, "words read from file.", "\n")
    # corrected words
    corrected_words = []
    corrected_word_count = 0
    for key in word_check.fixed_words:
        corrected_words.append(key)
        corrected_word_count += 1
    corrected_sort = sorted(corrected_words)
    print(corrected_word_count, "Corrected words")
    print(corrected_sort, "\n")
    #unknown words
    unknown_word_count = 0
    for word in word_check.unknown_words:
        unknown_word_count += 1
    unknown_sort = sorted(word_check.unknown_words)
    print(unknown_word_count, "Unknown words")
    print(unknown_sort)

# call to execute program
input_handle()
