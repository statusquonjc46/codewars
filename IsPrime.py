#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# By Nicholas Coletta, in the year 2019.
# This is part of my tour on codewars.com. The code below is a solution to a problem.

# INSTRUCTIONS: Define a function that takes an integer argument and returns logical value true or false depending on if the integer is a prime.
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# EXAMPLE:
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */

def is_prime(n):
    if n >= 2:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

print(is_prime(45))
