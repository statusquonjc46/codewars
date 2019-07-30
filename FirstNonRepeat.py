#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
# EXAMPLE:
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    initStr = string
    lowerStr = string.lower()
    firstChar = ''
    for letter in lowerStr:
        if lowerStr.count(letter) == 1:
            firstChar = letter
            break
    if firstChar in initStr:
        return firstChar
    elif firstChar.lower() in initStr:
        return firstChar.lower()
    elif firstChar.upper() in initStr:
        return firstChar.upper()

print(first_non_repeating_letter('aedqqdqdqwwwer'))
