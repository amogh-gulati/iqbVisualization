import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np
# x is P and y is Q
x = [0.5]
y = [0.5]
t = [1]
#iterating from time 1 to 1000
for i in range(1,1000):
    #print(i)
    xnext = x[i-1]*(1+1.3*(1-x[i-1]))-0.5*(x[i-1]*y[i-1])
    ynext = 0.3*y[i-1]+1.6*y[i-1]*x[i-1]
    if xnext  > 50*x[i-1] or ynext > 50*y[i-1]:
        break
    x.append(xnext)
    y.append(ynext) 
    t.append(i)

#print(x)
plt.plot(x,y)
#plt.plot(t,y)
plt.show()