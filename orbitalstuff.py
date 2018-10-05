#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

pi = np.pi

#inital conditions
x=1
y=0
vx=0
vy=2*pi
t=0
dt=0.001

x_array=[]
y_array=[]
vx_array=[]
vy_array=[]
t_array=[]

while t<1:
    r=np.sqrt(x**2+y**2)
    vx = vx - ((4*pi**2*x)/r**3)*dt
    x = x + vx*dt
    vy = vy - ((4*pi**2*y)/r**3)*dt
    y = y + vy*dt
    t=t+dt
    x_array.append(x)
    y_array.append(y)
    vx_array.append(vx)
    vy_array.append(vy)
    t_array.append(t)

plt.title('Orbit')
plt.xlabel('Astronomical Units in X')
plt.ylabel('Astronomical Units in Y')
plt.plot(x_array,y_array)
plt.show()
plt.title('Velocity in Vx')
plt.xlabel('time in years')
plt.ylabel('vx in AU/y')
plt.plot(t_array,vx_array)
plt.show()
plt.title('Velocity in Vy')
plt.xlabel('time in years')
plt.ylabel('vy in AU/y')
plt.plot(t_array,vy_array)
plt.show()

#We'll make use of Tkinter to animate this later

#Now let's consider a 3 body system, Sun, Earth, Jupiter
#F = GMjMe/rej^2

#inital conditions
x=1
y=0
vx=0
vy=2*pi
t=0
dt=0.001
xj=5
yj=0
vxj=0
vyj=0.1*pi #Figure this
Mj = 1.9e27
Ms=2.0e30
Me=6.0e24

xe_array=[]
ye_array=[]
xj_array=[]
yj_array=[]
while t<1:
    re = np.sqrt(x**2+y**2) #distance Earth-Sun
    rj = np.sqrt(xj**2+yj**2) #distance Jupiter - Sun
    rej = np.sqrt((x-xj)**2+(y-yj)**2) #distance Earth - Jupiter
    vx = vx - ((4*pi**2*x)/r**3)*dt-((4*pi**2*(Mj/Ms)*(x-xj))/rej**3)*dt #Earth x velocity
    vy = vy - ((4*pi**2*y)/r**3)*dt-((4*pi**2*(Mj/Ms)*(y-yj))/rej**3)*dt #Earth y velocity
    vxj = vxj - ((4*pi**2*xj)/rj**3)*dt-((4*pi**2*(Me/Ms)*(xj-x))/rej**3)*dt #Jupiter x velocity
    vyj = vyj - ((4*pi**2*yj)/rj**3)*dt-((4*pi**2*(Me/Ms)*(yj-y))/rej**3)*dt #Jupiter y velocity
    x = x + vx*dt #Earth positonal updates in x
    y = y + vy*dt #Earth positonal updates in y
    xj = xj + vxj*dt #Jupiters positional updates in x
    yj = yj + vyj*dt #Jupiters positional updates in y
    t=t+dt
    xe_array.append(x)
    ye_array.append(y)
    xj_array.append(xj)
    yj_array.append(yj)
plt.plot(xe_array,ye_array)
plt.show()
plt.plot(xj_array,yj_array)


# In[ ]:




