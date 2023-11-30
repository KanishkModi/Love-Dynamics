import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 1
b = 0.5
c = 1
d = 2


# function that returns dz/dt
def model(z,t):
    dxdt = a*z[0] + b*z[1]
    dydt = c*z[1] + d*z[0]
    dzdt = [dxdt,dydt]
    return dzdt

# initial condition
z0 = [1,0]

# time points
t = np.linspace(0,1)

# solve ODE
z = odeint(model,z0,t)

# plot results
plt.plot(t,z[:,0],'b-',label=r'$\frac{dx}{dt}=x+0.5y$')
plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}=y+2x$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
