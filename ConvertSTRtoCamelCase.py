#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# EXAMPLE:
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

import re
def to_camel_case(text):
    splitted = re.split(r'[-_\s]', text)
    print(splitted)
    newOne = [splitted[0]]
    for x in splitted[1:]:
        newOne.append(x.capitalize())
    return ''.join(newOne)
print(to_camel_case("the_pippi_Was_Omoshiroi"))
