def removeEven(p_list):

    """
    >>> removeEven([1,2,4,5,10,6,3])
    [1, 5, 3]


    :param p_list:
    :return:
    """

    unevenList = []
    for i in p_list:
        if i % 2 != 0:
            unevenList.append(i)

    return unevenList


def reomoveEven_listcomprehension(p_list):

    """
    >>> reomoveEven_listcomprehension([1,2,4,5,10,6,3])
    [1, 5, 3]

    :param p_list:
    :return:
    """

    return [oddNumber for oddNumber in p_list if oddNumber % 2 != 0]