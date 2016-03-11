# -*- coding: utf-8 -*-
"""
File: turtlestar.py
Copyright (c) 2016 Eddie Wadors
License: MIT
- allow user to input amount of sides and side length and make a nice little star.
"""

import turtle

num = raw_input("Please enter an odd natural number that is 5 or greater:")
side_len = raw_input("Please enter a side length:")
num_tips = int(num)
leng = int(side_len)

Eddie = turtle.Pen()
for x in range(num_tips):
    Eddie.forward(leng)
    Eddie.right((720+180*(num_tips-5))/num_tips)

end_prog = raw_input("Please press enter to exit window..." )
turtle.bye()
