import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 1
b = -1
c = -1
d = -2


# function that returns dz/dt
def model(z,t):
    dxdt = a + z[1]**2 + c*z[0]
    dydt = b + z[0]**2 + d*z[1]
    dzdt = [dxdt,dydt]
    return dzdt

# initial condition
z0 = [0.3,0.6]

# time points
t = np.linspace(0,10)

# solve ODE
z = odeint(model,z0,t)

# plot results
plt.plot(t,z[:,0],'b-',label=r'$\frac{dR}{dt}= 1+J^2-R$')
plt.plot(t,z[:,1],'r--',label=r'$\frac{dJ}{dt}=-1+R^2-2J$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
