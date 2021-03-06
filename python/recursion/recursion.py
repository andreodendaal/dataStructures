# Simple sum of numbers, non-recursive:

def listSum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

# TEST
# print(listSum([1,3,5,7,9]))


# Simple sum of numbers,recursive:
def listSumRecursive(numList):
    """ (numList) -> list

    Precondition: n >= 1

    Calculate the value of the list recursively

    >>> listSumRecursive([1,3,5,7,9]
    25
    >>> num_buses(1)
    1
    """
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSumRecursive(numList[1:])


def toString(n, base):
    """
    1. Reduce the original number to a series of single-digit numbers.
    2. Convert the single digit-number to a string using a lookup.
    3. Concatenate the single-digit strings together to form the final result.

    """
    convertString = "0123456789"
    if n < base:
        return convertString[n]
    else:
        return toString(n // base, base) + convertString[n % base]



if __name__ == '__main__':
    import timeit

    print(str(timeit.timeit("listSum([1, 3, 5, 7, 9])", setup="from __main__ import listSum"))+ " - listSum([1, 3, 5, 7, 9]")
    print(timeit.timeit("listSum([1, 3, 5, 7, 9, 3, 5, 7, 9])", setup="from __main__ import listSum"))
    print(timeit.timeit("listSum([1])", setup="from __main__ import listSum"))

    print(listSum([1, 3, 5, 7, 9]))

