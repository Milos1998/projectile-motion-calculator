import numpy as np
from matplotlib import pyplot as plt

V0= 240
g= -9.81
alfa= np.deg2rad(45)
ro= 1.23
C= 0.000785

Vx= V0 * np.cos(alfa)
Vy= V0 * np.sin(alfa)

t= 0
dt= 0.001

x=[0]
y=[0]

while y[-1] >= 0:
    v=np.sqrt(Vx**2+Vy**2)
    Vy+= dt*(g-ro*v*Vy*C/2)
    y.append(y[-1]+Vy*dt)
    
    Vx+= (-ro*Vx*v*C/2)*dt
    x.append(x[-1] + Vx*dt)


plt.plot(x, y)

plt.axis("equal")