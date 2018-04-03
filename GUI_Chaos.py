""" This is a script that will present the client with a simple GUI where he can specify the parameter r and the boundaries of x which will be used as input into plotting the chaotic behavior. The equation for the logistic map is xn+1 = r * xn * ( 1 - xn )"""

# from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt

class Chaos:

    def __init__(self,r,value_initial):
        self.r = r
        self.value = value_initial

    def update(self):
        self.value = self.r * self.value * (1 - self.value)

        return self.value

    def calc(self,steps):

        total_value = []

        for i in range(steps):

            total_value.append(self.value)
            self.update()

        return total_value

    def plotting(self):

        return





######################################################
"""Client to test the class"""

x = Chaos(2.5,0.5)
print(x.r)
print(x.value)
print(x.update())
print(x.calc(5))

