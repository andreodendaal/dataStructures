def findFirstUnique(lst):
    """
    Given a list, find the first integer which is unique in the list.
    Unique means the number does not repeat and appears only once in the whole list.
    Implement your solution in Python and see if it runs correctly!
    Edge case, no unique
    >>> findFirstUnique([4,5,5,2,0,2,4,0])
    []
    >>> findFirstUnique([9,2,3,2,6,6])
    9
    >>> findFirstUnique([4,5,1,2,0,4])
    5

    :param lst:
    :return:
    """
    reflst2 = []
    for ctr, value in enumerate(lst):

        reflst1 = lst[(ctr + 1):]
        if value not in reflst1 and value not in reflst2:
            return value
        else:
            reflst2.append(value)

    return []

