#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" An example that builds the graph which performs the following transformation:

		(1  0)      (1)
	z = (0 -1)* x + (1)
"""

from graph import Graph
from graph import Variable
from graph import Placeholder
from operations import matmul
from operations import add

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
