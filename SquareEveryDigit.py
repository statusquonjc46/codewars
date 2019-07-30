#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Welcome. In this kata, you are asked to square every digit of a number.
# EXAMPLE:
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

def square_digits(num):
    output = ''
    for i in str(num):
        sqr = int(i) * int(i)
        strOut = str(sqr)
        output += strOut
    return int(output)

print(square_digits(9119))
