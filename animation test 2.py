import numpy as np 
import matplotlib.pyplot as plt 

pi = np.pi
p = int(input('How many orbits would you like to see? '))
#Maybe I should make a list with (x,y,vx,vy,and vel) and call this list in the function
def PLANET(x,y,vx,vy):
    t=0
    dt=0.001
    clist = []
    xlist=[]
    ylist=[]
    while t<1: #t is in years this should correspond with the period of the last orbit you'd like to see
        r=np.sqrt(x**2+y**2)
        vx = vx - ((4*pi**2*x)/r**3)*dt
        x = x + vx*dt
        xlist.append(x)
        vy = vy - ((4*pi**2*y)/r**3)*dt
        y = y + vy*dt
        ylist.append(y)
        clist.append((x, y))
        t=t+dt
    return xlist,ylist,clist

ps = []
#ps.append([x,y,vx,vy]) #Velocity is in AU/year
orbit = []
ps.append([0.39,0,0,-10.210])    #Mercurey 0.24 years #vy = (x*2*pi)/period roughly 47.4 km/s
ps.append([0.723,0,0,-7.447])    #Venus    0.61 years 35.0 km/s
ps.append([1,0,0,-6.283])        #Earth    1.00 year  29.8 km/s
ps.append([1.524,0,0,-5.210])    #Mars     2.00 years 24.1 km/s
ps.append([5.203,0,0,-2.775])    #Jupiter  12.0 years 13.1 km/s
ps.append([9.539,0,0,-2.166])    #Saturn   29.0 years 9.70 km/s
ps.append([19.18,0,0,-1.421])    #Uranus   84.0 years 6.80 km/s
ps.append([30.06,0,0,-1.156])    #Neptune  163 years  5.40 km/s
ps.append([39.53,0,0,-1.013])    #Pluto    248 years  4.72 km/s
for i in range(8):
    orbit.append(PLANET(ps[i][0], ps[i][1], ps[i][2], ps[i][3]))

for i in range(p):
    plt.plot(orbit[i][0],orbit[i][1])
plt.show()

#Llist=[]
#Rlist=[]

#NOW LETS DO POLAR BABY WOO

y = np.array(orbit[3][1]) #Vector y 
x = np.array(orbit[3][0]) #Vector x
L = np.arctan2(y,x) #arctan2 accounts for the quadrent your angle is in
#Llist.append(L)
R = np.sqrt(x**2+y**2) #The magnitude of the vector
#Rlist.append(R)
ax=plt.subplot(111, polar = True)
plt.plot(L,R)
ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)
ax.set_title("Solar System Orbits")
ax.yaxis.labelpad=40
ax.set_ylabel("Distance from Sun (AU)", va='bottom')
plt.show()

 #Okay so we figured that out. Now we should generalize it for all the planets
 # We should also figure out how to display a single point on this graph and evolve the graph with time using MoviePy
 #I think the idea is we save a bazillion frames of the plot then play them frame by frame at 60 fps for a smooth animation. 
    


