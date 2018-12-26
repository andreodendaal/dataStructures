import timeit

def listBuildConcatenation():
    l = []
    for i in range(1000):
        l = l + [i]

def time_listBuildConcatenation():
    SETUP_CODE = ''' 
from __main__ import listBuildConcatenation'''

    TEST_CODE = '''listBuildConcatenation()'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # printing minimum exec. time
    #print('Build list with concatenation time: {}'.format(times))
    print(str(max(times)) + ' - max: Build list using CONCATENATION time')

def listBuildAppend():
    l = []
    for i in range(1000):
        l.append(i)

def time_listBuildAppend():
    SETUP_CODE = ''' 
from __main__ import listBuildAppend'''

    TEST_CODE = '''listBuildAppend()'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # printing minimum exec. time

    print(str(max(times)) + ' - max: Build list using APPEND time')

def listBuildComprehension():
    l = [i for i in range(1000)]

def time_listBuildComprehension():
    SETUP_CODE = ''' 
from __main__ import listBuildComprehension'''

    TEST_CODE = '''listBuildComprehension()'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # printing minimum exec. time

    print(str(max(times)) + ' - max: Build list using COMPREHENSION time')


def listBuildRange():
    l = list(range(1000))

def time_listBuildRange():
    SETUP_CODE = '''from __main__''' + ''' import listBuildRange'''

    TEST_CODE = '''listBuildRange()'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # printing minimum exec. time

    print(str(max(times)) + ' - max: Build list using RANGE function time')


if __name__ == "__main__":
    #time_listBuildConcatenation()
    #time_listBuildAppend()
    #time_listBuildComprehension()
    time_listBuildRange()
