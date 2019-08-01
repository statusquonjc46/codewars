#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
# EXAMPLE: rot13("EBG13 rknzcyr.") == "ROT13 example.";

def rot13(message):
    mesList = list(message)
    firstHalf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    secondHalf = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    punct = ['.', ',', '!', '?']
    lowerList = list(message.lower())
    decoded = []
    
    for letter in lowerList:
        if letter in firstHalf:
            for char in firstHalf:
                if char == letter:
                    opp = firstHalf.index(char)
                    decoded.append(secondHalf[opp])
        elif letter == ' ':
            decoded.append(letter)
        elif letter in secondHalf:
            for char in secondHalf:
                if char == letter:
                    opp = secondHalf.index(char)
                    decoded.append(firstHalf[opp])
        elif letter in punct:
            decoded.append(letter)
        else:
            decoded.append(letter)
    for x in range(len(decoded)):
        if mesList[x].isupper():
            decoded[x] = decoded[x].upper()
        
    return ''.join(decoded)

print(rot13("EBG13 rknzcyr."))