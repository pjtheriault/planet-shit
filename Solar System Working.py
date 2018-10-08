import numpy as np
import matplotlib.pyplot as plt
import time
#get_ipython().run_line_magic('matplotlib', 'inline')

pi = np.pi
#p = int(input('How many orbits would you like to see? '))
#Maybe I should make a list with (x,y,vx,vy,and vel) and call this list in the function
def PLANET(x,y,vx,vy):
    t=0
    dt=0.001
    clist = []
    while t<10: #t is in years
        r=np.sqrt(x**2+y**2)
        vx = vx - ((4*pi**2*x)/r**3)*dt
        x = x + vx*dt
        vy = vy - ((4*pi**2*y)/r**3)*dt
        y = y + vy*dt
        clist.append((x, y))
        t=t+dt
    return clist

ps = []
#ps.append([x,y,vx,vy]) #Velocity is in AU/year
orbit = []
ps.append([0.39,0,0,10.210])    #Mercurey 0.24 years #vy = (x*2*pi)/period roughly 47.4 km/s
ps.append([0.723,0,0,7.447])    #Venus    0.61 years 35.0 km/s
ps.append([1,0,0,6.283])        #Earth    1.00 year  29.8 km/s
ps.append([1.524,0,0,5.210])    #Mars     2.00 years 24.1 km/s
ps.append([5.203,0,0,2.775])    #Jupiter  12.0 years 13.1 km/s
ps.append([9.539,0,0,2.166])    #Saturn   29.0 years 9.70 km/s
ps.append([19.18,0,0,1.421])    #Uranus   84.0 years 6.80 km/s
ps.append([30.06,0,0,1.156])    #Neptune  163 years  5.40 km/s
ps.append([39.53,0,0,1.013])    #Pluto    248 years  4.72 km/s
for i in range(8):
    orbit.append(PLANET(ps[i][0], ps[i][1], ps[i][2], ps[i][3]))

#for i in range(p):
    #plt.plot(orbit[i][0],orbit[i][1])
#plt.show()

#Now let's animate this
#We already have all the information about the planets x and y positions stored in the array orbit
from tkinter import *
from sys import argv

def drawCircle(canvas, x, y, rad, fill):
    # color circle according to phase

    # draw a circle of given radius
    return canvas.create_oval(x-rad, y-rad, x+rad, y+rad, width=1, fill=fill)

def planet(canvas):

    s1 = "#FFD700"
    col = ["#0000CD", "#000000", "#DC143C"]
    #get the rest
    scale = 60
    xc = -orbit[4][1][0] * scale + 400 #0
    yc = 400
    radius_of_earth = scale / 23455 # 1/23455 is radius of earth/au
    radius_of_jupiter = scale / 2139.8
    sunrad = (radius_of_earth / 0.009158)
    prad = [radius_of_earth, radius_of_earth, radius_of_earth, radius_of_earth, radius_of_jupiter, radius_of_earth, radius_of_earth, radius_of_earth]
    sun = drawCircle(canvas, xc, yc, sunrad, s1)

    celbod = []

    for i in range(8):
        x = xc + (scale*orbit[i][1][0])
        y = yc + (scale*orbit[i][2][0])
        planettemp = drawCircle(canvas, x, y, prad[i], col[0]) #draws Earth on animation at starting point
        celbod.append(planettemp)
    canvas.after(1)
    gui.update()

    for t in range(1, len(orbit[0])):
        for p in range(8):
            canvas.delete(celbod[p])
            xl = xc + (scale*orbit[p][t-1][0])
            yl = yc + (scale*orbit[p][t-1][1])
            x = xc + (scale*orbit[p][t][0])
            y = yc + (scale*orbit[p][t][1])
            canvas.create_line(xl, yl, x, y, width= 1, fill="#000000")
            celbod[p] = drawCircle(canvas, x, y, prad[p], col[0])
        canvas.after(2)
        gui.update()
    

gui = Tk()
#root.mainloop()

width, height = 800, 800
x_center, y_center = 0.5*width, 0.5*height
x_scale, y_scale = 70, 70

# create a canvas
canvas = Canvas(gui, width=width, height=height, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_text(115, 25, font=("Purisa", 12), text="Earth's Orbit")

# begin recursive drawing
planet(canvas)


gui.mainloop()



