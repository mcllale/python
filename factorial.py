'''
This module provides two functions to calculate the factorial of a number:
1. Recursive approach
2. Iterative approach
Both functions handle negative input by returning -1.
The module also includes a simple test case to demonstrate the
functionality of both functions.
'''

def get_recursive_factorial(num):
    '''
    Calculates the factorial of a number using a recursive approach.
    
    Args:
        num: The number to calculate the factorial of.
    Returns:
        The factorial of num, or -1 if num is negative.
    '''
    if num < 0:
        return -1
    elif num < 2:
        return 1

    return num * get_recursive_factorial(num-1)


def get_iterative_factorial(num):
    '''
    Calculates the factorial of a number using an iterative approach.
    
    Args:
        num: The number to calculate the factorial of.
    Returns:
        The factorial of num, or -1 if num is negative.
    '''
    if num < 0:
        return -1

    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


# Test cases
print(get_recursive_factorial(3))
print(get_iterative_factorial(8))
