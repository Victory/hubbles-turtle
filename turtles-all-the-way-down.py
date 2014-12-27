#!/usr/bin/env python3

from turtle import *
from random import random
from time import sleep
from math import pi, sin, cos, sqrt

# TODO: make it so the hubble constant is around 70

h0 = 1 # hubble constant
c = 5 # speed of light

stars = list()
angles = list()
photons = list()
steps = 2
step = 2*pi / steps
hubbleturtle = Turtle(shape="turtle")
hubbleturtle.penup()
hubbleturtle.setpos((0, -100))

for ii in range(steps):
    angle = ii * step
    angles.append(angle)
    x = cos(angle) * random() * 200
    y = sin(angle) * random() * 200

    stars.append(Turtle(shape="triangle"))

    r = sqrt(x*x + y*y)
    if r < 100:
        color = "blue"
    else:
        color = "red"
        
    stars[ii].color(color)
    stars[ii].speed(10)
    stars[ii].penup()
    stars[ii].setpos((x, y))
    stars[ii].radians()
    stars[ii].setheading(angle)

    photons.append(Turtle(shape="circle"))
    photons[ii].penup()
    photons[ii].speed(10)
    photons[ii].color(color)
    photons[ii].setpos((x, y))
    photons[ii].radians()
    photons[ii].setheading(angle + pi)


screen = getscreen()
# should be like c/h0
inner_universe = 100
# cosmic scale factor
expanshion_rate = 1
# hubble flow
expanshion_step = .01

for i in range(200):
    #screen.tracer(1000)
     
    for ii, t in enumerate(stars):
        pos = t.pos()
        r = sqrt(pos[0]*pos[0] + pos[1]*pos[1])
        newr = r * expanshion_rate
        dr = newr - r
        t.forward(dr)

        # TODO: stop photons near origin
        pos = photons[ii].pos()
        r = sqrt(pos[0]*pos[0] + pos[1]*pos[1])
        newr = r * expanshion_rate
        dr = newr - r
        print(ii, dr)
        photons[ii].backward(dr)
        photons[ii].forward(c)

    hubbleturtle.pendown()
    hubbleturtle.circle(inner_universe)
    hubbleturtle.penup()
    inner_universe *= expanshion_rate
    expanshion_rate += expanshion_step
    
    hubbleturtle.setpos((0, -inner_universe))

    screen.update()
    sleep(.01)
sleep(3)
