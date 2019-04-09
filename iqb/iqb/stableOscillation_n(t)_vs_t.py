import matplotlib.pyplot as plt
a=2.7
nprev = 0.0001
nnext = 0
y = []
x = []
for z in range(100):
    nnext = a*nprev*(1-nprev)
    y.append(nnext)
    x.append(z)
    if abs(nprev-nnext)<0.0000001 :
        break
    nprev = nnext
    #nprev = nprev+0.01
plt.title("n(t+1) vs t")
plt.plot(x,y)
plt.show()