def findMinimum(arr):


    """
    >>> findMinimum([9,2,3,6])
    2

    >>> findMinimum([4, 5, 0, 3, 6])
    0

    :param arr:
    :return:
    """
    arr.sort()
    return arr[0]