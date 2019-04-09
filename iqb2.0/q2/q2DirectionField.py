import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np

fig = plt.figure(num=1)
ax=fig.add_subplot(111)

#Vector field
# X is P and Y is Q
X,Y = np.meshgrid( np.linspace(-0,1,20),np.linspace(1,2,20) )
#these are the difference equations
U = X*(1+1.3*(1-X)) - 0.5*X*Y - X
V = 0.3*Y + 1.6*X*Y - Y

#Normalize arrows
N = np.sqrt(U**2+V**2)
U2, V2 = U/N, V/N
ax.quiver( X,Y,U2, V2)


plt.xlim([0,1])
plt.ylim([1,2])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()
