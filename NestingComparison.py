#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structure as the first array.
# EXAMPLE:
# should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

# THIS ONLY PASSES THE USE CASES. I THINK IT WILL FAIL WITH OTHER TEST CASES...... ITS UGLY AND POOR PERFORMANCE/NOT PYTHONIC.... O^MILLION DEEP TRASH.
def same_structure_as(original,other):
    og = original
    other = other
    same = False
    for x in range(len(og)):
        print(x)
        if isinstance(og[x], list) and isinstance(other[x], list) and type(og[x][0]) != type (other[x][0]):
            return False
        else:
            if isinstance(og[x], list) and isinstance(other[x], list):
                if len(og[x]) == len(other[x]):
                    same = True
                else:
                    same = False
            elif isinstance(og[x], list) and isinstance(other[x], int):
                same = False
            else:
                same = True
    return same


print(same_structure_as([[[],[]]],[[1,1]]))
print(same_structure_as([1,[1,1]],[2,[2]]))
print(same_structure_as([1,[1,1]],[2,[2,2]]))
print(same_structure_as([1,[1,1]],[[2,2],2]))
print(same_structure_as([1,[1,1]],[[2,2],2]))