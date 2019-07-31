#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS:Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# EXAMPLE:
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

# This fails if the string 'True' or 'False' appear in the lists... 
def move_zeros(array):
    for x in range(len(array)):
        if array[x] is False:
            array[x] = 'False'
        elif array[x] is True:
            array[x] = 'True'
    for y in array:
        if y is 0:
            array.remove(y)
            array.append(0)
    for z in range(len(array)):
        if array[z] == 'False':
            array[z] = False
        elif array[z] == 'True':
            array[z] = True
    return array

print(move_zeros([1,2,0,1,False,0,1,0,3,0,1]))