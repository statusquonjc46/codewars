#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters, each taken only once - coming from s1 or s2.
# EXAMPLE:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    a = s1
    b = s2
    longString = list(a)
    rng = len(longString)
    newList = []

    for l in range(rng):
        if longString[l] not in newList:
            newList.append(longString[l])

    sortedStr = ''.join(sorted(newList))
    print (sortedStr)

    for letter in b:
        if letter not in sortedStr:
            sortedStr += letter
        else:
            print (letter + " is in longstring.")

    sortedStr = ''.join(sorted(sortedStr))
    print(sortedStr)
    return sortedStr

longest("aretheyhere", "yestheyarehere")
