# -*- coding: utf-8 -*-
"""
File: repeated_sqrt.py
Copyright (c) 2016 Eddie Wadors
License: MIT
- explaining a given code by the textbook using comments.
"""

from math import sqrt
for n in range(1, 60): #loop allows the variable to be square rooted once, and then square root it 59 times.
    r = 2.0
    for i in range(n):
        r = sqrt(r) #square root of the variable.
    for i in range(n):
        r = r**2 #square root of the square rooted variable.
    print '%d times sqrt and **2: %.16f' % (n, r)
