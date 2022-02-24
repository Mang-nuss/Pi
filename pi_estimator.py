"""
author:  MJ
date: 2021-10-29 -

the 'monte carlo' pi estimator uses a coordinate (x,y) to roughly calculate the value of pi.
A circle of radius=1 is placed within a square sized 2x2. (Hence, the area of the circle
equals pi, and the area of the square equals 4.) 2 random numbers are
picked; one for x,y, respectively. The point x,y is placed inside the circle if the hypothenuse
is less than or equal to 1, that is, if the square root of (x^2 + y^2) is less than or equal to 1. 
The ratio r between the insides and the totals times 4, is an estimation of pi.
"""

from random import uniform
import math

#--------------------------------#

def main():

    e = Estimator(10) # 10 decimals

    for n in range(20000): # 20000 attempts
        xval = uniform(-100,100)
        yval = uniform(-100,100)

        x = xval/100
        y = yval/100

        e.insideCheck(x,y)

    print("total nr of attempts were " + str(e.totals))
    print("total nr of inside hits were " + str(e.insides))
    print("pi = " + str(e.estimate()) + "\n")

#--------------------------------#

class Estimator:

    def __init__(self,nr):
        print("\n---PI-ESTIMATION---\n")
        self.insides = 0
        self.totals = 0
        self.dec = nr

    def insideCheck(self,x,y):
        self.totals += 1
        #print("the nr of total attempts is " + str(self.totals))
        position = x*x + y*y
        if math.sqrt(position) <= 1:
            self.insides += 1
            #print("position is inside circle. the nr of total insides is " + str(self.insides))
            #print("------------")
            return True;
        else:
            #print("position is outside circle" + "\n------------")
            return False;

    def estimate(self):
        i = self.insides * 10**self.dec
        t = self.totals
        value = (i/t) * 4
        #print("pi value is estimated to be " + str(value * 10**-10) + "\n------------")
        return value * 10**-self.dec

if __name__ == '__main__':
    main()
