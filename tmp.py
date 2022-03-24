import numpy as np
from matplotlib import pyplot as plt

V0= 240
g= 9.81
alfa= np.deg2rad(45)
ro= 1.23
C= 0.000785   #S= 0.25 Cx= 0.001
M= 1000
minM= 500
F= 10000


Vx= V0 * np.cos(alfa)
Vy= V0 * np.sin(alfa)

dt= 0.001

x=[0]
y=[0]

while y[-1] >= 0:
    if(M > minM):
        Fpx= F*np.cos(alfa)
        Fpy= F*np.sin(alfa)

        M-= 0.1
    else:
        Fpx= Fpy= 0
        
    Fx= Fpx - ro*Vx**2*C/2
    Fy= Fpy - g*M - ro*Vy**2*C/2 
    
    Vy+= dt*(Fx/M)
    y.append(y[-1]+Vy*dt)
    
    Vx+= dt*(Fy/M)
    x.append(x[-1] + Vx*dt)
    
    alfa= np.arctan2(y[-2]-y[-1], x[-2]-x[-1])

plt.plot(x, y)
