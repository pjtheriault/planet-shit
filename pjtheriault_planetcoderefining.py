#!/usr/bin/env python
# coding: utf-8

# In[19]:


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

#plt.title('Orbit')
#plt.xlabel('Astronomical Units in X')
#plt.ylabel('Astronomical Units in Y')
#plt.plot(x_array,y_array)
#plt.show()
#plt.title('Velocity in Vx')
#plt.xlabel('time in years')
#plt.ylabel('vx in AU/y')
#plt.plot(t_array,vx_array)
#plt.show()
#plt.title('Velocity in Vy')
#plt.xlabel('time in years')
#plt.ylabel('vy in AU/y')
#plt.plot(t_array,vy_array)
#plt.show()

#We'll make use of Tkinter to animate this later




#Maybe I should make a list with (x,y,vx,vy,and vel) and call this list in the function
def PLANET(x,y,vx,vy):
    t=0
    dt=0.001
    xlist = []
    ylist = []
    while t<250:
        r=np.sqrt(x**2+y**2)
        vx = vx - ((4*pi**2*x)/r**3)*dt
        x = x + vx*dt
        xlist.append(x)
        vy = vy - ((4*pi**2*y)/r**3)*dt
        y = y + vy*dt
        ylist.append(y)
        t=t+dt
    return xlist,ylist

ps = []
#ps.append([x,y,vx,vy])
orbit = []
ps.append([0.39,0,0,10.210])     #Mercurey .24 years #vy = (x*2*pi)/period roughly
ps.append([0.723,0,0,7.447])    #Venus .61 years
ps.append([1,0,0,6.283])       #Earth 1 year
ps.append([1.524,0,0,4.787])    #Mars 2 years
ps.append([5.203,0,0,2.775])  #Jupiter 12 years
ps.append([9.539,0,0,2.166])    #Saturn 29 years
ps.append([19.18,0,0,1.421])    #Uranus 84 years
ps.append([30.06,0,0,1.156])    #Neptune 163 years
ps.append([39.53,0,0,1.013])    #Pluto 248 years
for i in range(9):
    orbit.append(PLANET(ps[i][0], ps[i][1], ps[i][2], ps[i][3]))

plt.plot(orbit[8][0],orbit[8][1])


# In[ ]:




