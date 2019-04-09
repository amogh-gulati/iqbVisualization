import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np
#we use sympy to calculate the jacobian
import sympy as sm
pt, qt = sm.symbols('pt, qt', negative=False)
eqMat = sm.Matrix([pt*(1+1.3*(1-pt))-0.5*pt*qt,
0.3*qt+1.6*pt*qt])
Mat = sm.Matrix([ pt, qt ])
jacMat = eqMat.jacobian(Mat)
print('This is the Jacobian %s' % jacMat)

print("We take a value near the equilibrium to calculate eigenvalues and vectors")
print("p = 0.5 and q = 1.5")
expr = jacMat
a = expr.subs([(pt,1.5),(qt,1.5)])
#print(a)
b = np.array(a).astype(np.float64)
print(b)
eigVal,eigVec = np.linalg.eig(b)
print("these are the eigvals")
print(eigVal)
print("these are the eigVecs")
print(eigVec)
print("we cannot plot the eigenvectors on the real plane becuase they are complex")