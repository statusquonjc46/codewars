#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.
# EXAMPLE:
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord

import re
def camel_case(text):
    splitted = re.split(r'[-_\s]', text)
    print(splitted)
    newOne = []
    for x in splitted:
        newOne.append(x.capitalize())
    return ''.join(newOne)
