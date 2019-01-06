import timeit
import random

def dict_build_off_range(r1,r2,r3):

    construct_dict = {j: (j + 1) for j in range(r1)}
    #print(construct_dict)

    #for i in range(r1):
    #    print(i)
    #    construct_dict = {j: (j+1) for j in range(i)}
    #    print(construct_dict)

def time_dict_build():
    SETUP_CODE = '''from __main__''' + ''' import dict_build_off_range'''

    TEST_CODE = '''dict_build_off_range(10, 0, 0)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=4,
                          number=1000)

    # printing minimum exec. time

    print(str(times) + ' - max: Build dictionary using RANGE function time')



def list_build_off_range(r1,r2,r3):
    #construct_list = [j for j in range(r1)]
    construct_list = list(range(r1))
    #print(construct_list)

def time_list_build():
    SETUP_CODE = '''from __main__''' + ''' import list_build_off_range'''

    TEST_CODE = '''list_build_off_range(10, 0, 0)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=4,
                          number=1000)

    # printing minimum exec. time

    print(str(times) + ' - max: Build list using RANGE function time')

def timed_list_build():
    for i in range(10000, 1000001, 20000):
        x = list(range(i))
        lst_t = timeit.Timer("random.randrange(%d) in {}" % i % x, "import random")
        lst_time = lst_t.timeit(number=1)

        x = {j: None for j in range(i)}
        dct_t = timeit.Timer("random.randrange(%d) in {}" % i % x, "import random")
        d_time = dct_t.timeit(number=1)

        print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


if __name__=="__main__":
    timed_list_build()
    #time_dict_build()
    #time_list_build()


    #dict_build_off_range(10, 10, 2)
    #list_build_off_range(10, 10, 2)
