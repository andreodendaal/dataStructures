import timeit
import array


def arrayBuildConcatenation():
    newArray = array.array('d', [i for i in range(1000)])


def time_arrayBuildConcatenation():
    SETUP_CODE = ''' 
from __main__ import arrayBuildConcatenation'''

    TEST_CODE = '''arrayBuildConcatenation()'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # printing minimum exec. time
    #print('Build list with concatenation time: {}'.format(times))
    #print(str(times) + ' - max: Build ARRAY using CONCATENATION time')
    print('Build ARRAY using CONCATENATION - times: {}'.format(times))




if __name__ == "__main__":
    time_arrayBuildConcatenation()
    #time_listBuildAppend()
    #time_listBuildComprehension()
    #time_listBuildRange()
