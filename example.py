# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:31:00 2020

@author: ISH KAPOOR
"""
import turtle

colors = ["red","purple","blue","green","orange","yellow"]

my_pen = turtle.Pen()

turtle.bgcolor("black")

for x in range(360):
    my_pen.pencolor(colors[x % 8])
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(44)
