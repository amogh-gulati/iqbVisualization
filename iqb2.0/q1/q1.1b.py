import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np

fig = plt.figure(num=1)
ax=fig.add_subplot(111)

#projection array (enter the values)
a = 3
b = 0
c = 1
d = 2
arr = np.array([[a,b],[c,d]])


#Vector field
X,Y = np.meshgrid( np.linspace(-5,5,20),np.linspace(-10,10,20) )
U = (a-1)*X+b*Y
V = c*X+(d-1)*Y

#Normalize arrows
N = np.sqrt(U**2+V**2)
U2, V2 = U/N, V/N
ax.quiver( X,Y,U2, V2)


plt.xlim([-5,5])
plt.ylim([-10,10])
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()

print("there is no converging point in the plot hence it is unstable")