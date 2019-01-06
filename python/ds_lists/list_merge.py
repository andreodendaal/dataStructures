def mergeLists(list1, list2):
    """
    Implement a function which merges two sorted lists into another sorted list.
    Educative: Challenge 2
    Link - https://www.educative.io/collection/page/5642554087309312/5634727314718720/5655517842112512
    :param list1:
    :param list2: 
    :return:
    
    >>> mergeLists([1,3,4,5],[2,6,7,8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    mergeList = list1
    for elem in list2:
        mergeList.append(elem)
    mergeList.sort()
    return mergeList