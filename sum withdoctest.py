import doctest

def addTwoNumbers(a, b):
    '''
    Returns the sum of a and b

    >>> addTwoNumbers(2, 2)
    4
    >>> addTwoNumbers(4, 2)
    6
    >>> addTwoNumbers('4' , '2')
    '42'
    '''
    return a + b




doctest.testmod()