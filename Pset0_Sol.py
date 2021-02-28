#Ask the user to enter a number "x".
x = int(input("Enter number x: ")) 

#Ask the user to enter a number "y".
y = int(input("Enter numbet y: "))

#Print out number "x", raised to the power "y".
print("x**y = ",x**y)


#Prints out the log(base 2) of "x".

'''import math
print("log(x) = ",math.log(x,2))


import numpy
print("log(x) = ",numpy.log2(x))'''

import pylab
print("log(x) = ",pylab.log2(x))