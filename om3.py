import numpy as np
from matplotlib import pyplot as plt

V0= 240
g= -9.81
alfa= np.deg2rad(45)
ro= 1.23
C= 0.000785
M= 1000
minM= 500
F= 10000


Vx= V0 * np.cos(alfa)
Vy= V0 * np.sin(alfa)

dt= 0.001

x=[0]
y=[0]
while y[-1] >= 0:
    v= np.sqrt(Vx**2+Vy**2)
    if(M > minM):
        ap=F/M
        M-= 0.1
    else:
        ap= 0
    Vy+= dt*(g - ro*Vy*v*C/2 + ap*np.sin(alfa))
    y.append(y[-1]+Vy*dt)
    
    Vx+= dt*(-ro*Vx*v*C/2 + ap*np.cos(alfa))
    x.append(x[-1] + Vx*dt)
    
    
    
    alfa= np.arctan2(Vy, Vx)
    


plt.plot(x, y)