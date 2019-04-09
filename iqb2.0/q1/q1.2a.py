import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np

fig = plt.figure(num=1)
ax=fig.add_subplot(111)

#projection array (enter the values)
a = 1
b = -1
c = 2
d = 4
arr = np.array([[a,b],[c,d]])

#eigen vector and values

eigVal,eigVec = np.linalg.eig(arr)

print(eigVal)
print(eigVec)

print("The eigenvectors and the corresponding eigenvalues")
flag = 0
eq = 0
for i in range(eigVal.size):
    print("the eigen value is ",eigVal[i],end = " ")
    if eigVal.real[i] == 1:
        print("this is the equilibruim values")
        flag = 1
    if eigVal.real[i] >1:
        eq = 1
    print("corresponding vector " ,eigVec[:,i])

if flag ==0:
    print("as no eigenvalue is 1 the only equilibrium exit at [0,0]")
if eq ==1:
    print("as some eigenvector is greater than 1 the eq is unstable")
x = []
y = []
flag = 0
for i in range(eigVal.size):
    if eigVec[:,i][0].imag !=0 or eigVec[:,i][1].imag !=0:
        flag = 1
    x.append(eigVec[:,i][0])
    y.append(eigVec[:,i][1])

if flag==1:
    print("imaginary vectors these cannot be plotted in real plane")
else:
    #plt.plot(x,y)
    plt.plot([0,x[0]],[0,y[0]])
    plt.plot([0,x[1]],[0,y[1]])
    plt.show()
