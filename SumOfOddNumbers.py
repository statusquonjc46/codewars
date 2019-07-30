#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Calculate the row sums of this triangle from the row index (starting at index 1)
# EXAMPLE:
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def row_sum_odd_numbers(n):
    odds_list = []
    pyramid = []
    for i in range(20):
        if i % 2 != 0:
            odds_list.append(i)
    for j in range(0, len(odds_list)):
        pyramid = odds_list[j - 1:j + 1]
    print (pyramid)
row_sum_odd_numbers(4)
