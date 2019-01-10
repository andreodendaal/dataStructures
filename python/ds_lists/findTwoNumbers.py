def find_sum(lst, value):

    """
    Given a list and a number `n`, find two numbers from the list that sum to `n`.
    Implement your solution in Python and see if your output matches with the correct output.
    :param lst:
    :param value:
    :return:

    >>> find_sum([1,21,3,14,5,60,7,6], 81)
    [21, 60]

    """
    for first_value in lst:

        for i in lst:
            if i + first_value == value:
                return [first_value, i]

