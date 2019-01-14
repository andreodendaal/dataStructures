def findProduct(arr):

    """
    Given a list, return a list where each index stores the product of all numbers in the list except the number at the index itself.
    
    >>> findProduct([1,2,3,4])
    [24, 12, 8, 6]

    >>> findProduct([2, 5, 9, 3, 6])
    [810, 324, 180, 540, 270]
    
    :param lst: 
    :return: 
    """
    product_lst = []
    for ctr, value in enumerate(arr):
        # CLONE the list remember
        ref_lst = arr[:]

        # Remove the number at index
        del ref_lst[ctr]

        # Iterate through the changed list and multiply all the elements
        ctx = 1
        product_val = ref_lst[0]
        while ctx < len(ref_lst):
            product_val *= ref_lst[ctx]
            ctx += 1

        product_lst.append(product_val)

    return product_lst


