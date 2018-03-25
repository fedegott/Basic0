# Exercise for http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/BigONotation.html
# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list O(n2). The second function should be linear O(n)


import numpy as np
import time
import matplotlib.pyplot as plt
# First Function O(n^2)

# arr = np.random.normal(0,100,10)
# arr_round = np.round(arr,0)
N =50 # input size
total_time = []

for i in range(1,N):

    arr = np.random.randint(0,100,i)
    # print(arr)
    min = arr[0]
    start = time.time()
    for x in range(len(arr)):

        for y in range(len(arr)):
            # print(arr[x])
            # print(arr[y])
            # print(arr[x] < arr[y])

            if min > arr[y]:

                min = arr[y]
    print('The minimum is %d' %min)

    end = time.time()
    script_time = end - start
    print(script_time)
    total_time.append(script_time)


ax = plt.axes()
# fig = plt.figure()
#np.linspace( start, stop, num) stop is where to stop, num is number of samples to generate, whose default value is 50
x = np.linspace(1,N-1,N-1).round()
ax.plot(x,total_time)
ax.plot(x,x*x)
ax.set(title='time per input size',xlabel = 'time', ylabel= 'input size')
ax.grid()
plt.show()

#the plot should be a parabola.
#TODO: fit a N^2 parabole to the plot