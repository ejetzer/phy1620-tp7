#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

#import numpy as np
#
#rows = [[1,           1,  1,  1,  1],
#        [np.sqrt(3),  1,  0, -1, -np.sqrt(3)],
#        [1,           0, -1,  0,  1],
#        [np.sqrt(3), -1,  0,  1, -np.sqrt(3)],
#        [1,          -1,  1, -1,  1]]
#
#E = np.mat(np.array(rows))
#E_inv = E.getI()
#x_0 = np.array([[3, 0, np.sqrt(3), 2, 2]]).T
#A = 144 * E_inv * x_0
#print('A=', A)

import sympy as sp
sp.init_printing(use_unicode=True)

rows = [[1,           1,  1,  1,  1],
        [sp.sqrt(3),  1,  0, -1, -sp.sqrt(3)],
        [1,           0, -1,  0,  1],
        [sp.sqrt(3), -1,  0,  1, -sp.sqrt(3)],
        [1,          -1,  1, -1,  1]]

E = sp.Matrix(rows)
x_0 = sp.Matrix([3, 0, sp.sqrt(3), 2, 2])
A = 144 * E**-1 * x_0
A = sp.simplify(A)

print('A=', A)