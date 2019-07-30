#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Given a string of words, you need to find the highest scoring word.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.
# EXAMPLE: Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

def high(x):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abcdict = {}
    inputStr = x.split()
    cost = 1
    worddict = {}
    points = 0
    highest = 0
    highestWord = ''
    print (inputStr)
    for letter in abc:
        abcdict[letter] = cost
        cost += 1

    for word in inputStr:
        for char in word:
            if char in abcdict:
                points += abcdict[char]
                worddict[word] = points
        points = 0

    for key in worddict:
        if worddict[key] > highest:
            highest = worddict[key]
            highestWord = key
        elif worddict[key] == highest:
            if inputStr.index(key) < inputStr.index(highestWord):
                highestWord = key
                highest = worddict[key]

    print(highestWord, highest)

    return highestWord
high('izxjipuz qzwgoeeujl izxjipuz')
