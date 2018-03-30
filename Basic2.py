# Exercise for http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/BigONotation.html
# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list O(n2). The second function should be linear O(n)


import numpy as np
import time
import matplotlib.pyplot as plt
# First Function O(n^2)
##############################################################################
############## The first function should compare each number to every other number on the list O(n2)
# arr = np.random.normal(0,100,10)
# arr_round = np.round(arr,0)
# inputo = int(input('Do you want to see part O(N^2)(press 1) or O(logN) (press 2)?'))

# if inputo == 1:


total_time = []

def find_n2(N):

    for i in range(1, N):

        arr = np.random.randint(0, 100, i)
        # print(arr)
        min = arr[0] # first number in the list
        start = time.time()
        for x in range(len(arr)):

            for y in range(len(arr)):
                # print(arr[x])
                # print(arr[y])
                # print(arr[x] < arr[y])

                if min > arr[y]:
                    min = arr[y]
        print('The minimum is %d' % min)

        end = time.time()
        script_time = end - start
        print('the time it took is', script_time)
        total_time.append(script_time)

    ax = plt.axes()
    # fig = plt.figure()
    # np.linspace( start, stop, num) # stop is where to stop, num is number of samples to generate, whose default value is 50
    x = np.linspace(1, N - 1, N - 1).round()
    ax.plot(x, total_time)
    # ax.plot(x,x*x)
    ax.set(title='time per input size', xlabel='input size', ylabel='time')
    ax.grid()
    plt.show()

    # the plot should be a parabola.
    # TODO: fit a N^2 parabole to the plot

##############The second function should be linear O(n)

#### TIP: to INDENT a whole selected block just press TAB and SHIFT TAB for UNINDENT

# else:

def find_n(N):

    total_time = []

    for i in range(1, N):

        arr = np.random.randint(0, 100, i)
        # print(arr)
        min = arr[0]
        start = time.time()

        for x in range(len(arr)):

            if min > arr[x]:
                min = arr[x]
        print('The minimum is %d' % min)

        end = time.time()
        script_time = end - start
        print('the time it took is', script_time)
        total_time.append(script_time)

    ax = plt.axes()
    # # fig = plt.figure()
    # # np.linspace( start, stop, num) stop is where to stop, num is number of samples to generate, whose default value is 50
    x = np.linspace(1, N - 1, N - 1).round()
    ax.plot(x, total_time)
    # ax.plot(x,x*x)
    ax.set(title='time per input size', xlabel='input size', ylabel='time')
    ax.grid()
    plt.show()

N = 500  # input size
find_n(N)