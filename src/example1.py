#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An example that builds the graph which performs the following transformation:

		(1  0)      (1)
	z = (0 -1)* x + (1)
"""

from graph import Graph
from variable import Variable
from placeholder import Placeholder
from matmul import matmul
from add import add

# Create a new graph
Graph().as_default()

# Create variables
A = Variable([[1, 0], [0, -1]])
b = Variable([1,1])

# Create placeholder
x = Placeholder()

# Create hidden node y
y = matmul(A,x)

# Create output node z
z = add(y, b)
