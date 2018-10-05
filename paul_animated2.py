#!/usr/bin/env python
# coding: utf-8

# In[4]:

from Tkinter import *
from math import *
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

#inital conditions
def drawCircle(canvas, x, y, rad, fill):
    # color circle according to phase

    # draw a circle of given radius
    return canvas.create_oval(x-rad, y-rad, x+rad, y+rad, width=1, fill=fill)

def planet(canvas):
    x=1
    y=0
    vx=0
    vy=2*pi
    t=0
    dt=0.001
    xj=5 #Jupiter inital position in x
    yj=0 #Jupiter inital position  in y
    vxj=0 #Jupiter inital velocity in x
    vyj=2.755 #Jupiter inital velocity in y
    Mj = 1000*(1.9e27) #Mass of Jupiter 
    Ms=2.0e30 #Mass of Sun
    Me=6.0e24 #Mass of Earth

    yellow = "#FFD700"
    blue = "#0000CD"
    black = "#000000"
    crimson = "#DC143C"
    xc = 400
    yc = 400
    scale = 70
    sunrad = scale/3
    erad = scale/20
    jrad = scale/10
    sun = drawCircle(canvas, xc, yc, sunrad, yellow)
    xe_array=[]
    ye_array=[]
    xj_array=[]
    yj_array=[]
    tj_array=[]
    vxe_array=[]
    xpl = xc + (scale*x)
    ypl = yc + (scale*y)
    xjpl = xc + (scale*xj)
    yjpl = yc + (scale*yj)
    xp = 0
    yp = 0
    xjp = 0
    yjp = 0
    planet = drawCircle(canvas, xpl, ypl, erad, blue)
    jupiter = drawCircle(canvas, xjpl, yjpl, jrad, crimson)
    canvas.after(1)
    gui.update()
    while t<12: #Note that this is in years and the orbital period of Jupiter is 12 Earth Years
        re = np.sqrt(x**2+y**2) #distance Earth-Sun
        rj = np.sqrt(xj**2+yj**2) #distance Jupiter - Sun
        rej = np.sqrt((x-xj)**2+(y-yj)**2) #distance Earth - Jupiter
        vx = vx - ((4*pi**2*x)/re**3)*dt-((4*pi**2*(Mj/Ms)*(x-xj))/rej**3)*dt #Earth x velocity
        vy = vy - ((4*pi**2*y)/re**3)*dt-((4*pi**2*(Mj/Ms)*(y-yj))/rej**3)*dt #Earth y velocity
        vxj = vxj - ((4*pi**2*xj)/rj**3)*dt-((4*pi**2*(Me/Ms)*(xj-x))/rej**3)*dt #Jupiter x velocity
        vyj = vyj - ((4*pi**2*yj)/rj**3)*dt-((4*pi**2*(Me/Ms)*(yj-y))/rej**3)*dt #Jupiter y velocity
        x = x + vx*dt #Earth positonal updates in x
        y = y + vy*dt #Earth positonal updates in y
        xj = xj + vxj*dt #Jupiters positional updates in x
        yj = yj + vyj*dt #Jupiters positional updates in y
        t=t+dt
        xp = xc + (scale*x)
        yp = yc + (scale*y)
        xjp = xc + (scale*xj)
        yjp = yc + (scale*yj)
        canvas.create_line(xp, yp, xpl, ypl,fill = black, width=1)
        canvas.delete(planet)
        planet = drawCircle(canvas, xp, yp, erad, blue)
        canvas.create_line(xjp, yjp, xjpl, yjpl,fill = black, width=1)
        canvas.delete(jupiter)
        jupiter = drawCircle(canvas, xjp, yjp, jrad, crimson)
        canvas.after(1)
        gui.update()
        xpl = xp
        ypl = yp
        xjpl = xjp
        yjpl = yjp
        xe_array.append(x)
        ye_array.append(y)
        xj_array.append(xj)
        yj_array.append(yj)
        tj_array.append(t)
        vxe_array.append(vx)

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