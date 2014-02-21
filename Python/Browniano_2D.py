import sys
import numpy as np
import matplotlib.pyplot as plt

x=0
y=0
d=[0]
n=int(sys.argv[1])
a=2*np.pi*np.random.random(n)

for i in range(n):
    s=np.sin(a[i])
    c=np.cos(a[i])
    x=x+s
    y=y+c
    u=np.sqrt((x**2)+(y**2))
    d.append(u)
    plt.plot(d)

ax = plt.axes()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Movimiento Browniano, "+str(n)+" iteraciones")

filename = 'Browniano_2D_'+str(n) 
plt.savefig(filename + '.pdf',format = 'pdf', transparent=False)
    
