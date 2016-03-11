# -*- coding: utf-8 -*-
"""
File: turtlepoly.py
Copyright (c) 2016 Eddie Wadors
License: MIT
- allow the user to input data and create a shape using turtle.
"""

import turtle

string_1 = raw_input ("Enter a number of sides:")
side_number = int (string_1)
string_2 = raw_input ("Enter side length:")
length_number = int (string_2)


def draw_reg_polygon(t, num_sides, side_len):
     for i in range(num_sides):
        t.forward(side_len)
        t.left(360.0/num_sides)
    
bob = turtle.Pen()
for j in range(1):
    draw_reg_polygon(bob,side_number,length_number)
 
stopper = raw_input("Hit <enter> to quit.")

turtle.bye()
