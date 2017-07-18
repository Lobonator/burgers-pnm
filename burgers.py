import numpy as np
import matplotlib.pyplot as plt


Nx = 400
Nt = 200

Tmax = 1
Xmax = 2
n = 0
C = 0.8
t = 0.0  
v = np.zeros(Nx)
vn = np.zeros(Nx)

dx = Xmax/Nx
v0 = np.zeros(Nx)
x = np.zeros(Nx)

for i in range(0,Nx):
    x[i]=i*dx
    
for i in range(0,Nx):
    if x[i] <= 0.25: 
        v[i] = 3
    if x[i] > 0.25 and x[i] <= 0.65:
        v[i] = 2
    if x[i] > 0.65 and x[i] < 1:
        v[i] = 1
dt = C*dx/np.abs(np.nanmax(v))
plt.ion()

while t < Tmax:
    t += dt
    for i in range(1,Nx-2):
        vn[i] = 1/2*( v[i+1] + v[i-1] ) - (dt/dx)*(1/2)*( (v[i+1])**2/2 - (v[i-1])**2/2 )
    vn[0] = v[1]
    vn[Nx-1] = v[Nx-2]
 
    v = np.copy(vn)
    if n%5==0:
        plt.plot(x,v)  
        plt.pause(0.01)
        plt.clf()
   
    n += 1



        
        



    # print(max(u[:,0]))
    # for n in range(0,Nt-1):
    #     for i in range(1,Nx-1):
    #         u[i, n+1] =  0.5*(u[i+1,n] + u[i-1,n]) - C/4*((u[i+1,n])**2 - (u[i-1,n])**2) 
    #     u[0,n+1]=u[Nx-2,n]
    #     u[Nx-1,n+1] = u[0,n]