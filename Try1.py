import webbrowser
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# webbrowser.open('http://www.google.com', new=2) # webbrowser will open the website
# webbrowser.open_new_tab('http://www.google.com')

a = np.array([[1,2,3],[4,5,6]])

print(a[1,2])

b = random.uniform(0,1)
print(b)

np.random.seed(1)
c =np.random.normal(0,1,1000)
print(c)
plt.subplot(211)
plt.hist(c,50)
# plt.show()

x = np.random.normal(0,1,100)
y = np.random.normal(0,1,100)
plt.subplot(212)
plt.plot(x,y)
plt.show()