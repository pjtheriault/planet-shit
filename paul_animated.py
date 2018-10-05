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
    yellow = "#FFD700"
    blue = "#0000CD"
    black = "#000000"
    xc = 400
    yc = 400
    scale = 300
    sunrad = 25
    erad = 7.5
    sun = drawCircle(canvas, xc, yc, sunrad, yellow)
    x_array=[]
    y_array=[]
    vx_array=[]
    vy_array=[]
    t_array=[]
    xpl = xc + (scale*x)
    ypl = yc + (scale*y)
    xp = 0
    yp = 0
    planet = drawCircle(canvas, xpl, ypl, erad, blue)
    canvas.after(1)
    gui.update()
    while t<10:
        r=np.sqrt(x**2+y**2)
        vx = vx - ((4*pi**2*x)/r**3)*dt
        x = x + vx*dt
        vy = vy - ((4*pi**2*y)/r**3)*dt
        y = y + vy*dt
        t=t+dt
        xp = xc + (scale*x)
        yp = yc + (scale*y)
        canvas.create_line(xp, yp, xpl, ypl,fill = black, width=1)
        canvas.delete(planet)
        planet = drawCircle(canvas, xp, yp, erad, blue)
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