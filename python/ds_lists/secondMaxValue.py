def findSecondMaximum(lst):
    """
    Given an array of size n, can you find the second maximum element in the list?
    Implement your solution in Python and see if your output matches the correct output!

    >>> findSecondMaximum([9,2,3,6])
    6

    >>> findSecondMaximum([4, 2, 1, 5, 0])
    4

    >>> findSecondMaximum([5])
    False

    :param lst:
    :return:
    """

    lst.sort(reverse=True)
    if len(lst) < 2:
        return False
    else:
        return lst[1]
