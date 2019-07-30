#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS:
def format_duration(seconds):
    inTime = seconds
    day = inTime // (24 * 3600)
    inTime = inTime % (24 * 3600)
    hour = inTime // 3600
    inTime %= 3600
    minutes = inTime // 60
    inTime %= 60
    newSeconds = inTime
    retDays = f'{day} days'
    retHours = f'{hour} hours'
    retMinutes = f'{minutes} minutes'
    retSeconds = f'{newSeconds} seconds'
    
    if newSeconds == 1:
        retSeconds = f'{newSeconds} second'
    if newSeconds == 0:
        retSeconds = ''
    if minutes == 1:
        retMinutes = f'{minutes} minute'
    if minutes == 0:
        retMinutes = ''
    if hour == 1:
        retHours = f'{hour} hour'
    if hour == 1:
        retHours = ''
    if day == 1:
        retDays = f'{day} day'
    if day == 0:
        retDays = ''
    
    if day > 0 and hour > 0 and minutes > 0 and newSeconds > 0:
        return f'{retDays}, {retHours}, {retMinutes}, and {retSeconds}'
    elif day == 0 and hour > 0 and minutes > 0 and newSeconds > 0:
        return f'{retHours}, {retMinutes}, and {retSeconds}'
    elif day == 0 and hour == 0 and minutes > 0 and newSeconds > 0:
        return f'{retMinutes} and {retSeconds}'
    elif day == 0 and hour == 0 and minutes == 0 and newSeconds > 0:
        return f'{retSeconds}'
    elif day > 0 and hour == 0 and minutes > 0 and newSeconds > 0:
        return f'{retDays}, {retMinutes}, and {retSeconds}'
    elif day > 0 and hour == 0 and minutes == 0 and newSeconds > 0:
        return f'{retDays} and {retSeconds}'
    elif day > 0 and hour == 0 and minutes == 0 and newSeconds == 0:
        return f'{retDays}'
    elif day > 0 and hour > 0 and minutes == 0 and newSeconds > 0:
        return f'{retDays}, {retHours} and {retSeconds}'
    elif day > 0 and hour > 0 and minutes == 0 and newSeconds == 0:
        return f'{retDays} and {retHours}'
    elif day > 0 and hour > 0 and minutes > 0 and newSeconds == 0:
        return f'{retDays}, {retHours} and {retMinutes}'
    
    
    

print(format_duration(31557600))
    

