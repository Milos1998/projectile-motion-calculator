import numpy as np
from matplotlib import pyplot as plt

V0= 240
g= -9.81
alfa= np.deg2rad(45)


Vx= V0 * np.cos(alfa)
Vy= V0 * np.sin(alfa)

dt= 0.001

x=[0]
y=[0]

while y[-1] >= 0:
    Vy+= dt*g
    y.append(y[-1]+Vy*dt)
    
    x.append(x[-1] + Vx*dt)


plt.plot(x, y)