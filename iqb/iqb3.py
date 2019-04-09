import matplotlib.pyplot as plt
import numpy as np
#this will move u in below loop form 1.4 to 4 in 260 steps (0.01 units between each) 
P=np.linspace(1.4,4,260)
m=0
x = []
y = []
for u in P:
    x.append(u)
    #returns float between 0 and 1
    m = np.random.random()
    for n in range(1001):
      m=(u*m)*(1-m)    #where would that m converge basically
    for l in range(1051):
      m=(u*m)*(1-m)
    # Collection of data in Y must be done once per value of u
    y.append(m)
#this would show small points not lines
plt.plot(x,y,'o')
plt.show()