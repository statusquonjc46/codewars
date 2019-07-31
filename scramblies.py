#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
# EXAMPLE:
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False
from collections import Counter
def scramble(s1, s2):
    sone = Counter(s1)
    stwo = Counter(s2)
    diff = stwo - sone
    if len(diff) == 0:
        return True
    else:
        return False
# Both sets of code work. The commented is slower by about 2000ms. Which this challenge relied on performance.
''' compList = []
    for letter in s1:
        if letter in s2:
            if s2.count(letter) > compList.count(letter):
                compList.append(letter)
    print(compList)
    if len(compList) == len(s2):
        return True
    else:
        return False'''
    
print(scramble('rkqodlw', 'world')) 