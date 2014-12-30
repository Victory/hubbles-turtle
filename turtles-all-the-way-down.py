#!/usr/bin/env python3

from turtle import *
from random import random
from time import sleep
from math import pi, sin, cos, sqrt

dt = 1.0 # time step
age = 3.0 # age of the universe
c = 20.0 # speed of light
# hubble length
hubble_length = c*age
# hubble constant
h0 = 1/c # hubble constant
# cosmic scale factor
cosmic_scale_factor = 1.1
cosmic_scale_step = .01
print(age)


stars = list()
angles = list()
photons = list()
steps = 4
step = 2*pi / steps
hubbleturtle = Turtle(shape="turtle")
hubbleturtle.penup()


for ii in range(steps):



    angle = ii * step
    angles.append(angle)
    x = cos(angle) * random() * 5 * hubble_length
    y = sin(angle) * random() * 5 * hubble_length

    stars.append(Turtle(shape="triangle"))

    r = sqrt(x*x + y*y)
    if r < hubble_length:
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
    #photons[ii].penup()
    photons[ii].speed(10)
    photons[ii].color(color)
    photons[ii].setpos((x, y))
    photons[ii].radians()
    photons[ii].setheading(angle + pi)


screen = getscreen()

hubbleturtle.setpos((0, -hubble_length))

for i in range(200):
    #screen.tracer(1000)

    distance_light_travels_per_step = c * dt * cosmic_scale_factor

    print(cosmic_scale_factor)

    for ii, t in enumerate(stars):
        pos = t.pos()
        r = sqrt(pos[0]*pos[0] + pos[1]*pos[1])
        newr = r * cosmic_scale_factor
        dr = newr - r
        t.forward(dr)

        # TODO: stop photons near origin

        pos = photons[ii].pos()

        r = sqrt(pos[0]*pos[0] + pos[1]*pos[1])
        print(pos, r)
        if r < 20:
            continue

        photons[ii].forward(distance_light_travels_per_step)
        pos = photons[ii].pos()
        r = sqrt(pos[0]*pos[0] + pos[1]*pos[1])
        newr = r * cosmic_scale_factor
        dr = newr - r
        print(ii, dr, distance_light_travels_per_step)
        #photons[ii].backward(dr)


    # accelerting universe
    cosmic_scale_factor += cosmic_scale_step


    hubbleturtle.pendown()
    hubbleturtle.circle(hubble_length)
    hubbleturtle.penup()
    hubble_length += distance_light_travels_per_step
    
    hubbleturtle.setpos((0, -hubble_length))

    screen.update()
    sleep(.01)
sleep(3)
