import matplotlib.pyplot as plt
a=1.7
nprev = 0.0001
nnext = 0   
y = []
x = []
while nprev<1:
    nnext = a*nprev*(1-nprev)
    y.append(nnext)
    x.append(nprev)
    nprev = nprev+0.01
plt.title("n(t+1) vs n(t)")
plt.plot(x,y)
#drawing x=y
plt.plot([0,1],[0,1])
#cobweb starting point
nprev = 0.01
x = [nprev]
y = [0]
nc = 1
nnext = 0
ncount = 0
while nc!=nnext and ncount<20:
    ncount+=1
    nc = nnext
    nnext = a*nprev*(1-nprev)
    y.append(nnext)
    x.append(nprev)
    nprev = nnext
    y.append(nprev)
    x.append(nprev)
if ncount==1000:
    print("not converging")
#print(x)
#print(y)
plt.plot(x,y)
plt.show()