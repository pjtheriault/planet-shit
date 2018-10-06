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
def force(xy, r, starmass):
    r0 = 0.2
    if(r < r0):
        r = r0
    return starmass*xy/(r**3)

def drawCircle(canvas, x, y, rad, fill):
    # color circle according to phase

    # draw a circle of given radius
    return canvas.create_oval(x-rad, y-rad, x+rad, y+rad, width=1, fill=fill)

def planet(canvas):
    x=0
    y=0
    vx=5
    vy=-12.2
    t=0
    dt=0.001
    yellow = "#FFD700"
    blue = "#0000CD"
    black = "#000000"
    crimson = "#DC143C"
    green = "#006400"
    xc = 600
    yc = 400

    scale = 200
    sunrad = 25
    erad = 7.5
    xs1 = -1
    ys1= -0.5
    xs2 = 1
    ys2 = -0.5
    xs3 = 0
    ys3 = 0.5
    xps1 = xc + (scale*xs1)
    yps1= yc + (scale*ys1)
    xps2 = xc + (scale*xs2)
    yps2 = yc + (scale*ys2)
    xps3 = xc + (scale*xs3)
    yps3 = yc + (scale*ys3)
    sun = drawCircle(canvas, xps1, yps1, sunrad, yellow)
    sun2 = drawCircle(canvas, xps2, yps2, sunrad, blue)
    sun3 = drawCircle(canvas, xps3, yps3, sunrad, crimson)
    x_array=[]
    y_array=[]
    vx_array=[]
    vy_array=[]
    t_array=[]
    xpl = xc + (scale*x)
    ypl = yc + (scale*y)
    xp = 0
    yp = 0
    planet = drawCircle(canvas, xpl, ypl, erad, green)
    canvas.after(1)
    gui.update()
    smass = 50
    while t<20:
        r1=np.sqrt((x-xs1)**2+(y-ys1)**2)
        r2=np.sqrt((x-xs2)**2+(y-ys2)**2)
        r3=np.sqrt((x-xs3)**2+(y-ys3)**2)
        this1 = force(x-xs1,r1,smass) + force(x-xs2,r2,smass) + force(x-xs3,r3,smass)
        this2 = force(y-ys1,r1,smass) + force(y-ys2,r2,smass) + force(y-ys3,r3,smass)
        #print(this1, this2)
        vx = vx - this1*dt
        x = x + vx*dt
        vy = vy - this2*dt
        y = y + vy*dt
        t=t+dt
        xp = xc + (scale*x)
        yp = yc + (scale*y)
        canvas.create_line(xp, yp, xpl, ypl,fill = black, width=1)
        canvas.delete(planet)
        planet = drawCircle(canvas, xp, yp, erad, green)
        canvas.after(10)
        gui.update()
        xpl = xp
        ypl = yp
        x_array.append(x)
        y_array.append(y)
        vx_array.append(vx)
        vy_array.append(vy)
        t_array.append(t)

gui = Tk()
#root.mainloop()

width, height = 1200, 800
x_center, y_center = 0.5*width, 0.5*height
x_scale, y_scale = 70, 70

# create a canvas
canvas = Canvas(gui, width=width, height=height, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_text(115, 25, font=("Purisa", 12), text="Earth's Orbit")

# begin recursive drawing
planet(canvas)


gui.mainloop()